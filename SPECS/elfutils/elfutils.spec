# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           elfutils
Version:        0.194
Release:        %autorelease
Summary:        Higher-level library to access ELF files
License:        GPL-3.0-or-later
URL:            https://sourceware.org/elfutils/
VCS:            git:https://sourceware.org/git/elfutils.git
#!RemoteAsset
Source0:        https://sourceware.org/elfutils/ftp/%{version}/%{name}-%{version}.tar.bz2
BuildSystem:    autotools

# from https://sourceware.org/git/?p=elfutils.git;a=commit;h=4a5cf8be906d5991e7527e69e3f2ceaa74811301
Patch0:         elfutils-0.194-fix-const.patch

BuildOption(conf):  --program-prefix=eu-
BuildOption(conf):  --disable-debuginfod
BuildOption(conf):  --enable-libdebuginfod=dummy
BuildOption(conf):  --enable-deterministic-archives

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  rpm-devel
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libmicrohttpd)

%description
elfutils is a collection of utilities and libraries to read, create
and modify ELF binary files, find and handle DWARF debug data,
symbols, thread state and stacktraces for processes and core files.

%package        devel
Summary:        Development files for libasm and libdw
License:        GPL-2.0-or-later OR LGPL-3.0-or-later
Requires:       pkgconfig(libelf)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the headers and libraries needed to build
applications that require libasm and libdw.

%package     -n libelf
Summary:        Library to read and write ELF files
License:        GPL-2.0-or-later OR LGPL-3.0-or-later

%description -n libelf
This package provides a high-level library to read and write ELF files.
This is part of the elfutils package.

%package     -n libelf-devel
Summary:        Development files for libelf
Requires:       libelf%{?_isa} = %{version}-%{release}
License:        GPL-2.0-or-later OR LGPL-3.0-or-later

%description -n libelf-devel
This package contains the headers and libraries needed to build
applications that require libelf.

%package     -n libdebuginfod-dummy
Summary:        Library for build-id HTTP ELF/DWARF server
Provides:       libdebuginfod = %{version}-%{release}
License:        GPL-2.0-or-later OR LGPL-3.0-or-later

%description -n libdebuginfod-dummy
The libdebuginfod package contains shared libraries
dynamically loaded from -ldw, which use a debuginfod service
to look up debuginfo and associated data. Also includes a
command-line frontend.
The package is dummy.

%package     -n libdebuginfod-dummy-devel
Summary:        Libraries and headers to build debuginfod client applications
License:        GPL-2.0-or-later OR LGPL-3.0-or-later
Provides:       libdebuginfod-devel = %{version}-%{release}
Requires:       libdebuginfod-dummy = %{version}-%{release}

%description -n libdebuginfod-dummy-devel
The libdebuginfod-devel package contains the libraries
to create applications to use the debuginfod service.
The package is dummy.

%package     -n debuginfod-dummy-client
Summary:        Command line client for build-id HTTP ELF/DWARF server
Provides:       debuginfod-client = %{version}-%{release}

%description -n debuginfod-dummy-client
The elfutils-debuginfod-client package contains a command-line frontend.
The package is dummy.

%conf -p
autoreconf -fiv
chmod a+x tests/run*.sh

%install -a
# remove unneeded files
rm -f %{buildroot}/%{_sysconfdir}/profile.d/debuginfod.*sh
rm -f %{buildroot}%{_datadir}/fish/vendor_conf.d/debuginfod.fish
rm -f %{buildroot}%{_mandir}/man8/debuginfod*.8*
rm -rf %{buildroot}/%{_datadir}/fish
ls -lR %{buildroot}/%{_libdir}/libelf*

# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS NOTES README THANKS TODO
%{_bindir}/eu-addr2line
%{_bindir}/eu-ar
%{_bindir}/eu-elfclassify
%{_bindir}/eu-elfcmp
%{_bindir}/eu-elfcompress
%{_bindir}/eu-elflint
%{_bindir}/eu-findtextrel
%{_bindir}/eu-make-debug-archive
%{_bindir}/eu-nm
%{_bindir}/eu-objdump
%{_bindir}/eu-ranlib
%{_bindir}/eu-readelf
%{_bindir}/eu-size
%{_bindir}/eu-stack
%{_bindir}/eu-strings
%{_bindir}/eu-strip
%{_bindir}/eu-unstrip
%{_bindir}/eu-srcfiles
# libasm
%{_libdir}/libasm.so.*
%{_libdir}/libasm-%{version}.so
# libdw
%{_libdir}/libdw.so.*
%{_libdir}/libdw-%{version}.so
# man
%{_mandir}/man1/*.1*

%files devel
# libasm
%{_libdir}/libasm.so
%{_libdir}/libasm.a
%dir %{_includedir}/elfutils
%{_includedir}/elfutils/libasm.h
# libdw
%{_libdir}/libdw.a
%{_libdir}/libdw.so
%{_includedir}/dwarf.h
%dir %{_includedir}/elfutils
%{_includedir}/elfutils/libdw.h
%{_includedir}/elfutils/libdwelf.h
%{_includedir}/elfutils/libdwfl.h
%{_includedir}/elfutils/libdwfl_stacktrace.h
%{_includedir}/elfutils/known-dwarf.h
%{_libdir}/pkgconfig/libdw.pc

%files -n libelf
%{_libdir}/libelf.so.*
%{_libdir}/libelf-%{version}.so

%files -n libelf-devel
%{_libdir}/libelf.so
%{_libdir}/libelf.a
%{_includedir}/libelf.h
%{_includedir}/gelf.h
%{_includedir}/nlist.h
%dir %{_includedir}/elfutils
%{_includedir}/elfutils/elf-knowledge.h
%{_includedir}/elfutils/version.h
%{_libdir}/pkgconfig/libelf.pc
%{_mandir}/man3/elf_*.3*
%{_mandir}/man3/elf32_*.3*
%{_mandir}/man3/elf64_*.3*
%{_mandir}/man3/gelf_*.3*
%{_mandir}/man3/libelf.3.gz

%files -n libdebuginfod-dummy
%{_libdir}/libdebuginfod.so.*
%{_libdir}/libdebuginfod-%{version}.so

%files -n libdebuginfod-dummy-devel
%{_mandir}/man3/debuginfod_*.3*
%dir %{_includedir}/elfutils
%{_includedir}/elfutils/debuginfod.h
%{_libdir}/libdebuginfod.so
%{_libdir}/pkgconfig/libdebuginfod.pc

%files -n debuginfod-dummy-client
%{_bindir}/debuginfod-find
%{_mandir}/man1/debuginfod-find.1*
%{_mandir}/man7/debuginfod-client-config.7*

%changelog
%{?autochangelog}
