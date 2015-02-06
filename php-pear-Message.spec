%define		_class		Message
%define		upstream_name	%{_class}

Name:		php-pear-%{upstream_name}
Version:	0.6
Release:	15
Summary:	Message hash and digest (HMAC) generation methods and classes
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Message/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Classes for message hashing and HMAC signature generation using the
mhash functions.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/README
%doc %{upstream_name}-%{version}/misc
%{_datadir}/pear/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml



%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6-13mdv2012.0
+ Revision: 742134
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6-12
+ Revision: 679406
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6-11mdv2011.0
+ Revision: 613720
- the mass rebuild of 2010.1 packages

* Wed Nov 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.6-10mdv2010.1
+ Revision: 470172
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.6-10mdv2010.0
+ Revision: 441353
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.6-9mdv2009.1
+ Revision: 322371
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.6-8mdv2009.0
+ Revision: 236973
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.6-7mdv2007.0
+ Revision: 82207
- Import php-pear-Message

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.6-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.6-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.6-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.6-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.6-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.6-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.6-1mdk
- initial Mandriva package (PLD import)

