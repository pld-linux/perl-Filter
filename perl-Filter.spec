%include	/usr/lib/rpm/macros.perl
Summary:	Filter perl module
Summary(pl):	Modu³ perla Filter
Name:		perl-Filter
Version:	1.17
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Filter/Filter-%{version}.tar.gz
Patch:		perl-Filter-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Filter package consists of a number of Source Filters.

%description -l pl
Pakiet Filter zawiera zestaw filtrów ¼róde³.

%prep
%setup -q -n Filter-%{version}
%patch -p0

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}
make install DESTDIR=$RPM_BUILD_ROOT

cp -r examples/* $RPM_BUILD_ROOT/usr/src/examples/%{name}

find $RPM_BUILD_ROOT%{perl_sitearch}/auto/Filter -name \*.so \
	-exec strip --strip-unneeded {} \;

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Filter
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%dir %{perl_sitearch}/Filter
%{perl_sitearch}/Filter/Util
%{perl_sitearch}/Filter/*.pm

%dir %{perl_sitearch}/auto/Filter
%{perl_sitearch}/auto/Filter/.packlist

%dir %{perl_sitearch}/auto/Filter/Util/Call
%{perl_sitearch}/auto/Filter/Util/Call/Call.bs
%attr(755,root,root) %{perl_sitearch}/auto/Filter/Util/Call/Call.so

%dir %{perl_sitearch}/auto/Filter/Util/Exec
%{perl_sitearch}/auto/Filter/Util/Exec/Exec.bs
%attr(755,root,root) %{perl_sitearch}/auto/Filter/Util/Exec/Exec.so

%dir %{perl_sitearch}/auto/Filter/decrypt
%{perl_sitearch}/auto/Filter/decrypt/decrypt.bs
%attr(755,root,root) %{perl_sitearch}/auto/Filter/decrypt/decrypt.so

%dir %{perl_sitearch}/auto/Filter/tee
%{perl_sitearch}/auto/Filter/tee/tee.bs
%attr(755,root,root) %{perl_sitearch}/auto/Filter/tee/tee.so

%{_mandir}/man3/*

/usr/src/examples/%{name}
