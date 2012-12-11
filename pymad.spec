Summary: A wrapper for the MAD MPEG Audio decoder library
Name:    pymad
Version: 0.6
Release: 5
Source0: http://spacepants.org/src/pymad/download/%{name}-%{version}.tar.gz
License: GPL
Group: Development/Python
BuildRequires: libmad-devel
BuildRequires: python-devel
Url: http://spacepants.org/src/pymad/

%description
pymad is a Python wrapper for the MPEG Audio Decoder library.

Access this module via "import mad" or "from mad import *".  To decode
an mp3 stream, you'll want to create a MadFile object and read data from
that.  You can then write the data to a sound device.  See the example
program in test/ for a simple mp3 player that uses libao for the sound
device.


%prep
%setup -q

%build
python config_unix.py
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files 
%doc README AUTHORS NEWS THANKS
%py_platsitedir/*




%changelog
* Fri Nov 04 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.6-4mdv2012.0
+ Revision: 717573
- rebuild

* Wed Nov 03 2010 GÃ¶tz Waschk <waschk@mandriva.org> 0.6-3mdv2011.0
+ Revision: 592876
- rebuild for new python 2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.6-2mdv2011.0
+ Revision: 441988
- rebuild

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 0.6-1mdv2009.1
+ Revision: 319569
- rebuild with python 2.6
- new release 0.6

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.5.4-6mdv2009.0
+ Revision: 259426
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.5.4-5mdv2009.0
+ Revision: 247294
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- fix description
- remove URL from description

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Tue Nov 28 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.5.4-3mdv2007.0
+ Revision: 88190
- Import pymad

* Tue Nov 28 2006 Götz Waschk <waschk@mandriva.org> 0.5.4-3mdv2007.1
- update file list

* Thu Jun 29 2006 Götz Waschk <waschk@mandriva.org> 0.5.4-2mdv2007.0
- Rebuild

* Tue Jun 28 2005 Götz Waschk <waschk@mandriva.org> 0.5.4-1mdk
- New release 0.5.4

* Tue Apr 26 2005 Götz Waschk <waschk@mandriva.org> 0.5.3-1mdk
- New release 0.5.3

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.5.2-2mdk
- Rebuild for new python

* Fri Nov 05 2004 Goetz Waschk <waschk@linux-mandrake.com> 0.5.2-1mdk
- New release 0.5.2

