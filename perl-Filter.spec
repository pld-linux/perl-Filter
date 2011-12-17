%include	/usr/lib/rpm/macros.perl
Summary:	Source filters
Summary(pl.UTF-8):	Filtry źródeł 
Name:		perl-Filter
Version:	1.39
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Filter/Filter-%{version}.tar.gz
# Source0-md5:	1bddf1632b2e1f78ad07aae5c476a137
Patch0:		%{name}-paths.patch
URL:		http://search.cpan.org/dist/Filter/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Filter package consists of a number of source filters.  Source filters
alter the program text of a module before Perl sees it, much as a C
preprocessor alters the source text of a C program before the compiler
sees it.

%description -l pl.UTF-8
Pakiet Filter zawiera zestaw filtrów źródeł. Filtry źródeł ingerują w
tekst kodu modułu zanim zobaczy go Perl, podobnie jak robi to
preprocesor C zanim kompilator ujrzy kod.

%prep
%setup -q -n Filter-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"
rm -f decrypt/*.bak examples/*.orig

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

find examples -name '*.bak' -exec rm -f '{}' ';'
cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/Filter
%{perl_vendorarch}/Filter/Util
%{perl_vendorarch}/Filter/*.pm
%dir %{perl_vendorarch}/auto/Filter
%dir %{perl_vendorarch}/auto/Filter/Util
%dir %{perl_vendorarch}/auto/Filter/Util/Call
%{perl_vendorarch}/auto/Filter/Util/Call/Call.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Filter/Util/Call/Call.so
%dir %{perl_vendorarch}/auto/Filter/Util/Exec
%{perl_vendorarch}/auto/Filter/Util/Exec/Exec.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Filter/Util/Exec/Exec.so
%dir %{perl_vendorarch}/auto/Filter/decrypt
%{perl_vendorarch}/auto/Filter/decrypt/decrypt.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Filter/decrypt/decrypt.so
%dir %{perl_vendorarch}/auto/Filter/tee
%{perl_vendorarch}/auto/Filter/tee/tee.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Filter/tee/tee.so
%{perl_vendorarch}/filter-util.pl
%{_mandir}/man3/Filter*.3pm*
%{_mandir}/man3/perlfilter.3pm*
%{_examplesdir}/%{name}-%{version}
