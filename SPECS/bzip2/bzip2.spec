# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define soname_version 1.0

Name:           bzip2
Version:        1.0.8
Release:        %autorelease
Summary:        File compression utility
License:        BSD-4-Clause
URL:            https://sourceware.org/bzip2
#!RemoteAsset
Source0:        https://sourceware.org/pub/%{name}/%{name}-%{version}.tar.gz
#!RemoteAsset
Source1:        https://sourceware.org/pub/%{name}/%{name}-%{version}.tar.gz.sig
Source2:        bzip2.pc
BuildSystem:    autotools

BuildOption(build):  -f Makefile-libbz2_so

BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
Bzip2 is a freely available, patent-free, high quality data compressor.
Bzip2 compresses files to within 10 to 15 percent of the capabilities
of the best techniques available.  However, bzip2 has the added benefit
of being approximately two times faster at compression and six times
faster at decompression than those techniques.  Bzip2 is not the
fastest compression utility, but it does strike a balance between speed
and compression capability.

Install bzip2 if you need a compression utility.

%package        devel
Summary:        Libraries and header files for apps which will use bzip2
Requires:       bzip2%{?_isa} = %{version}-%{release}

%description    devel
Header files and a library of bzip2 functions, for developing apps
which will use the library.

# No configure
%conf

%prep -a
# Use our own bzip2.pc
cp -a %{SOURCE2} .
sed -i "s|^libdir=|libdir=%{_libdir}|" bzip2.pc

%build -a
# Build again
rm -f *.o
make bzip2 bzip2recover

%install
# Why...
chmod 644 bzlib.h
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_libdir}/pkgconfig,%{_includedir}}
cp -p bzlib.h $RPM_BUILD_ROOT%{_includedir}
install -m 755 libbz2.so.%{version} $RPM_BUILD_ROOT%{_libdir}
install -m 644 libbz2.a $RPM_BUILD_ROOT%{_libdir}
install -m 644 bzip2.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/bzip2.pc
install -m 755 bzip2-shared  $RPM_BUILD_ROOT%{_bindir}/bzip2
install -m 755 bzip2recover bzgrep bzdiff bzmore  $RPM_BUILD_ROOT%{_bindir}/
cp -p bzip2.1 bzdiff.1 bzgrep.1 bzmore.1  $RPM_BUILD_ROOT%{_mandir}/man1/
ln -s bzip2 $RPM_BUILD_ROOT%{_bindir}/bunzip2
ln -s bzip2 $RPM_BUILD_ROOT%{_bindir}/bzcat
ln -s bzdiff $RPM_BUILD_ROOT%{_bindir}/bzcmp
ln -s bzmore $RPM_BUILD_ROOT%{_bindir}/bzless
ln -s bzgrep $RPM_BUILD_ROOT%{_bindir}/bzegrep
ln -s bzgrep $RPM_BUILD_ROOT%{_bindir}/bzfgrep
ln -s libbz2.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libbz2.so.%{soname_version}
ln -s libbz2.so.%{soname_version} $RPM_BUILD_ROOT%{_libdir}/libbz2.so.1
ln -s libbz2.so.1 $RPM_BUILD_ROOT%{_libdir}/libbz2.so
ln -s bzip2.1 $RPM_BUILD_ROOT%{_mandir}/man1/bzip2recover.1
ln -s bzip2.1 $RPM_BUILD_ROOT%{_mandir}/man1/bunzip2.1
ln -s bzip2.1 $RPM_BUILD_ROOT%{_mandir}/man1/bzcat.1
ln -s bzdiff.1 $RPM_BUILD_ROOT%{_mandir}/man1/bzcmp.1
ln -s bzmore.1 $RPM_BUILD_ROOT%{_mandir}/man1/bzless.1
ln -s bzgrep.1 $RPM_BUILD_ROOT%{_mandir}/man1/bzegrep.1
ln -s bzgrep.1 $RPM_BUILD_ROOT%{_mandir}/man1/bzfgrep.1

%files
%doc CHANGES README
%license LICENSE
%{_bindir}/*
%{_mandir}/*/*
%{_libdir}/libbz2.so.1*

%files devel
%doc manual.html manual.pdf
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/bzip2.pc
%{_libdir}/libbz2.a

%changelog
%autochangelog
