%include	/usr/lib/rpm/macros.perl
Summary:	Filter perl module
Summary(pl):	Modu³ perla Filter
Name:		perl-Filter
Version:	1.29
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Filter/Filter-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filter package consists of a number of Source Filters.

%description -l pl
Pakiet Filter zawiera zestaw filtrów ¼róde³.

%prep
%setup -q -n Filter-%{version}
%patch -p0

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_sitearch}/Filter
%{perl_sitearch}/Filter/Util
%{perl_sitearch}/Filter/*.pm
%dir %{perl_sitearch}/auto/Filter
%dir %{perl_sitearch}/auto/Filter/Util
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
%{perl_sitearch}/filter-util.pl
%{_mandir}/man3/*
%{_examplesdir}/%{name}
