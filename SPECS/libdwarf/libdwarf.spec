# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libdwarf
Version:        2.2.0
Release:        %autorelease
Summary:        Library to access DWARF debugging information
License:        LGPL-2.1-only AND BSD-2-Clause-FreeBSD
URL:            https://www.prevanders.net/dwarf.html
VCS:            git:https://github.com/davea42/libdwarf-code
#!RemoteAsset
Source0:        https://github.com/davea42/libdwarf-code/releases/download/v%{version}/libdwarf-%{version}.tar.xz
Patch0:         libdwarf-both.patch
BuildSystem:    meson

BuildOption(conf):  -Ddwarfgen=true
BuildOption(conf):  --default-library=both

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)

%description
Libdwarf is a library of functions to provide read/write DWARF
debugging records.

%package        devel
Summary:        Library and header files of libdwarf
License:        LGPL-2.1-only AND BSD-2-Clause-FreeBSD
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Libdwarf-devel provides the libraries and header files for libdwarf.

%package        static
Summary:        Static libdwarf library
License:        LGPL-2.1-only AND BSD-2-Clause-FreeBSD
Requires:       %{name}-devel = %{version}-%{release}

%description    static
Libdwarf-static provides the static libdwarf library.

%package        tools
Summary:        Tools for accessing DWARF debugging information
License:        GPL-2.0-only AND BSD-2-Clause-FreeBSD

%description    tools
Libdwarf-tools provides C++ version of dwarfdump (dwarfdump2) command-line utilities
to access DWARF debug information.

%files
%license src/lib/libdwarf/{COPYING,LIBDWARFCOPYRIGHT,LGPL.txt}
%doc src/lib/libdwarf/{ChangeLo,README}
%{_libdir}/libdwarf.so.2
%{_libdir}/libdwarf.so.2.*
%{_libdir}/libdwarfp.so.2
%{_libdir}/libdwarfp.so.2.*

%files devel
%doc doc/*.pdf
%{_includedir}/libdwarf-2
%{_libdir}/pkgconfig/libdwarf.pc
%{_libdir}/libdwarf.so
%{_libdir}/libdwarfp.so

%files static
%{_libdir}/libdwarf.a
%{_libdir}/libdwarfp.a

%files tools
%license src/bin/dwarfdump/{COPYING,DWARFDUMPCOPYRIGHT,GPL.txt}
%{_bindir}/dwarfdump
%{_bindir}/dwarfgen
%{_datadir}/dwarfdump/dwarfdump.conf
%{_mandir}/man1/dwarfdump.1*
%{_mandir}/man1/dwarfgen.1*

%changelog
%autochangelog
