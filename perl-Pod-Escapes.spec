%define	upstream_name	 Pod-Escapes
%define upstream_version 1.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Perl module to resolve Pod E<...> sequences
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/S/SB/SBURKE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Pod::Simple is a module to resolve Pod E<...> sequences.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
make test

%files
%doc ChangeLog README
%{perl_vendorlib}/Pod
%{_mandir}/man3/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.40.0-4mdv2012.0
+ Revision: 765597
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.40.0-3
+ Revision: 764125
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.40.0-2
+ Revision: 667295
- mass rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.40.0-1mdv2011.0
+ Revision: 404293
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.04-8mdv2009.0
+ Revision: 223998
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.04-7mdv2008.1
+ Revision: 180531
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 1.04-6mdv2008.0
+ Revision: 23320
- rebuild


* Mon Apr 03 2006 Buchan Milne <bgmilne@mandriva.org> 1.04-5mdk
- Rebuild
- use mkrel

* Mon Jun 06 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-4mdk 
- better url
- spec cleanup
- drop useless directories
- make test in %%check

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.04-3mdk 
- removed MANIFEST
- added missing doc files
- fixed summary

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.04-2mdk
- fix buildrequires in a backward compatible way

* Tue May 11 2004 Michael Scherer <misc@mandrake.org> 1.04-1mdk
- New release 1.04

* Sun Apr 04 2004 Michael Scherer <misc@mandrake.org> 1.03-2mdk
- rebuild to correct upload ( noticed by guillaumovitch )

* Fri Apr 02 2004 Michael Scherer <misc@mandrake.org> 1.03-1mdk
- First MandrakeSoft Package

