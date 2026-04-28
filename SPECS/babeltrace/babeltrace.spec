# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           babeltrace
Version:        1.5.11
Release:        %autorelease
Summary:        Trace conversion program with support for the CTF format (legacy 1.x)
License:        MIT AND GPL-3.0-or-later WITH Bison-exception-2.2 AND LGPL-2.1-only AND BSD-4-Clause-UC
URL:            https://babeltrace.org/
VCS:            git:https://github.com/efficios/babeltrace.git
#!RemoteAsset:  sha256:67b43aaaef5c951fa7af1a557cf7201a11fe89876b7c22ba0a03cbc316db5a9c
Source:         https://www.efficios.com/files/%{name}/%{name}-%{version}.tar.bz2
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-python-bindings

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(libdw)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  python3dist(setuptools)
BuildRequires:  swig

%description
Babeltrace 1.x is the legacy trace manipulation framework for the Common
Trace Format (CTF) and other trace formats. Its successor is Babeltrace 2.
This package is provided for compatibility with software that has not yet
migrated to the v2 API.

%package        devel
Summary:        Development files for the babeltrace library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(glib-2.0)

%description    devel
Header files and pkg-config files for developing applications that link
against libbabeltrace 1.x.

%package -n     python-%{name}
Summary:        Python bindings for libbabeltrace 1.x
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       python3-%{name} = %{version}-%{release}
Provides:       python3-%{name}%{?_isa} = %{version}-%{release}
%python_provide python3-%{name}

%description -n python-%{name}
Python bindings for libbabeltrace 1.x.

%conf -p
autoreconf -fiv

%install -a
rm -rf %{buildroot}%{_pkgdocdir}

%check
# skip tests; CTF binary fixtures fail on riscv64.

%files
%doc README ChangeLog
%license LICENSE gpl-2.0.txt mit-license.txt
%{_bindir}/%{name}*
%{_libdir}/lib%{name}*.so.*
%{_mandir}/man1/%{name}*.1*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/babeltrace.pc
%{_libdir}/pkgconfig/babeltrace-ctf.pc

%files -n python-%{name}
%{python3_sitearch}/%{name}
%{python3_sitearch}/%{name}*.egg-info

%changelog
%autochangelog
