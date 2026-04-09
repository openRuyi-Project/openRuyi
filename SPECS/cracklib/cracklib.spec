# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define dictdir %{_datadir}/cracklib
%define dictpath %{dictdir}/pw_dict

Name:           cracklib
Version:        2.10.3
Release:        %autorelease
Summary:        A password-checking library
License:        LGPL-2.1-or-later
URL:            https://github.com/cracklib/cracklib
#!RemoteAsset
Source0:        https://github.com/cracklib/cracklib/releases/download/v%{version}/cracklib-%{version}.tar.gz
#!RemoteAsset
Source1:        https://github.com/cracklib/cracklib/releases/download/v%{version}/cracklib-words-%{version}.gz
BuildSystem:    autotools

BuildOption(conf):  --with-pic
BuildOption(conf):  --without-python
BuildOption(conf):  --with-default-dict=%{dictpath}
BuildOption(conf):  --disable-static
BuildOption(install):  'pythondir=${pyexecdir}'

BuildRequires:  gettext
BuildRequires:  pkgconfig(zlib)

# The cracklib-format script calls gzip, but without a specific path.
Requires:       gzip

%description
CrackLib tests passwords to determine whether they match certain
security-oriented characteristics, with the purpose of stopping users
from choosing passwords that are easy to guess. CrackLib performs
several tests on passwords: it tries to generate words from a username
and gecos entry and checks those words against the password; it checks
for simplistic patterns in passwords; and it checks for the password
in a dictionary.

CrackLib is actually a library containing a particular C function
which is used to check the password, as well as other C
functions. CrackLib is not a replacement for a passwd program; it must
be used in conjunction with an existing passwd program.

Install the cracklib package if you need a program to check users'
passwords to see if they are at least minimally secure. If you install
CrackLib, you will also want to install the cracklib-dicts package.

%package        devel
Summary:        Development files needed for building applications which use cracklib
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The cracklib-devel package contains the header files and libraries needed
for compiling applications which use cracklib.

%package        dicts
Summary:        The standard CrackLib dictionaries
BuildRequires:  make
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    dicts
The cracklib-dicts package includes the CrackLib dictionaries.
CrackLib will need to use the dictionary appropriate to your system,
which is normally put in /usr/share/dict/words. Cracklib-dicts also
contains the utilities necessary for the creation of new dictionaries.

If you are installing CrackLib, you should also install cracklib-dicts.

%conf -p
# Use the dictionary from the build to test
sed -i 's,util/cracklib-check <,util/cracklib-check $(DESTDIR)/$(DEFAULT_CRACKLIB_DICT) <,' Makefile.in

%conf -a
# Update the .gmo files
make -C po update-gmo

%install -a
gunzip -c %{SOURCE1} | ./util/cracklib-format | \
./util/cracklib-packer %{buildroot}%{dictpath}
./util/cracklib-format %{buildroot}%{dictdir}/cracklib-small | \
./util/cracklib-packer %{buildroot}%{dictdir}/cracklib-small
rm -f %{buildroot}%{dictdir}/cracklib-small
sed s,/usr/lib/cracklib_dict,%{dictpath},g lib/crack.h > %{buildroot}%{_includedir}/crack.h
ln -s cracklib-format %{buildroot}%{_sbindir}/mkdict
# packer link removed as it clashes with hashicorp's packer binary.
#ln -s cracklib-packer %{buildroot}/%{_sbindir}/packer
touch %{buildroot}/top

toprelpath=..
touch %{buildroot}/top
while ! test -f %{buildroot}%{_libdir}/$toprelpath/top ; do
      toprelpath=../$toprelpath
done
rm -f %{buildroot}/top
if test %{dictpath} != %{_libdir}/cracklib_dict ; then
ln -s $toprelpath%{dictpath}.hwm %{buildroot}%{_libdir}/cracklib_dict.hwm
ln -s $toprelpath%{dictpath}.pwd %{buildroot}%{_libdir}/cracklib_dict.pwd
ln -s $toprelpath%{dictpath}.pwi %{buildroot}%{_libdir}/cracklib_dict.pwi
fi
rm -f %{buildroot}%{_libdir}/python*/site-packages/_cracklib*.*a
rm -f %{buildroot}%{_libdir}/libcrack.la

mkdir -p %{buildroot}%{_mandir}/man{3,8}
install -p -m644 doc/*.3 %{buildroot}%{_mandir}/man3/
install -p -m644 doc/*.8 %{buildroot}%{_mandir}/man8/
if ! test -s %{buildroot}%{_mandir}/man8/cracklib-packer.8 ; then
    echo .so man8/cracklib-format.8 > %{buildroot}%{_mandir}/man8/cracklib-packer.8
fi
if ! test -s %{buildroot}%{_mandir}/man8/cracklib-unpacker.8 ; then
    echo .so man8/cracklib-format.8 > %{buildroot}%{_mandir}/man8/cracklib-unpacker.8
fi

%find_lang %{name} --generate-subpackages

%files
%doc README README-WORDS NEWS README-LICENSE AUTHORS
%license COPYING.LIB
%{_libdir}/libcrack.so.*
%dir %{_datadir}/cracklib
%{dictpath}.*
%{_datadir}/cracklib/cracklib.magic
%{_sbindir}/*cracklib*
%{_mandir}/man8/*

%files devel
%{_includedir}/*
%{_libdir}/libcrack.so
%{_mandir}/man3/*

%files dicts
%{_datadir}/cracklib/cracklib-small.*
%{_libdir}/cracklib_dict.*
%{_sbindir}/mkdict

%changelog
%autochangelog
