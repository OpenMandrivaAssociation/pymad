%define name pymad
%define version 0.5.4
%define release %mkrel 6

Summary: A wrapper for the MAD MPEG Audio decoder library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://spacepants.org/src/pymad/download/%{name}-%{version}.tar.bz2
License: GPL
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libmad-devel
BuildRequires: libpython-devel
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
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc README AUTHORS NEWS THANKS
%py_platsitedir/*


