# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           bcc
Version:        0.36.1
Release:        %autorelease
Summary:        BPF Compiler Collection (BCC)
License:        Apache-2.0
URL:            https://github.com/iovisor/bcc
#!RemoteAsset:  sha256:3b16f1eb6a5b90a5a68686c0f4195455f1c58da5ae40f004e931c19e98fa8d98
Source0:        https://github.com/iovisor/bcc/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DREVISION_LAST=%{version}
BuildOption(conf):  -DREVISION=%{version}
BuildOption(conf):  -DPYTHON_CMD=python3
BuildOption(conf):  -DCMAKE_USE_LIBBPF_PACKAGE:BOOL=TRUE
BuildOption(conf):  -DENABLE_NO_PIE=OFF
BuildOption(conf):  -DENABLE_LLVM_SHARED=1

BuildRequires:  gcc-c++
BuildRequires:  bison
BuildRequires:  cmake >= 2.8.7
BuildRequires:  flex
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libdebuginfod)
BuildRequires:  llvm-devel
BuildRequires:  clang-devel
BuildRequires:  llvm-static
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  libbpf-devel
BuildRequires:  libbpf-static
BuildRequires:  zip

Requires:       libbpf
Requires:       tar

Recommends:     linux-devel
Recommends:     %{name}-tools = %{version}-%{release}

%description
BCC is a toolkit for creating efficient kernel tracing and manipulation
programs, and includes several useful tools and examples. It makes use
of eBPF (Extended Berkeley Packet Filters), a feature that was first
added to Linux 3.15. Much of what BCC uses requires Linux 4.1 and above.

%package        devel
Summary:        Shared library for BPF Compiler Collection (BCC)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Suggests:       debuginfod-dummy-client

%description    devel
The %{name}-devel package contains libraries and header files for developing
application that use BPF Compiler Collection (BCC).

%package        doc
Summary:        Examples for BPF Compiler Collection (BCC)
Requires:       man
Requires:       texinfo
Recommends:     python3-%{name} = %{version}-%{release}
Recommends:     %{name}-lua = %{version}-%{release}
BuildArch:      noarch

%description    doc
Examples for BPF Compiler Collection (BCC)

%package     -n python-bcc
Summary:        Python bindings for BPF Compiler Collection (BCC)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       python3-bcc
%python_provide python3-bcc
BuildArch:      noarch

%description -n python-bcc
Python3 bindings for BPF Compiler Collection (BCC)

%package        lua
Summary:        Standalone tool to run BCC tracers written in Lua
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    lua
Standalone tool to run BCC tracers written in Lua

%package        tools
Summary:        Command line tools for BPF Compiler Collection (BCC)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-%{name} = %{version}-%{release}
Requires:       python3dist(netaddr)

%description    tools
Command line tools for BPF Compiler Collection (BCC)

%package     -n libbpf-tools
Summary:        Command line libbpf tools for BPF Compiler Collection (BCC)
BuildRequires:  libbpf-devel
BuildRequires:  libbpf-static
BuildRequires:  bpftool

%description -n libbpf-tools
Command line libbpf tools for BPF Compiler Collection (BCC)

%build -a
pushd libbpf-tools
%make_build BPFTOOL=%{_sbindir}/bpftool LIBBPF_OBJ=%{_libdir}/libbpf.a
popd

%install -a
pushd libbpf-tools
%make_install DESTDIR=./tmp-install prefix=
(
    cd tmp-install/bin
    for file in *; do
        mv $file bpf-$file
    done
    # now fix the broken symlinks
    for file in `find . -type l`; do
        dest=$(readlink "$file")
        ln -s -f bpf-$dest $file
    done
)
mkdir -p %{buildroot}/%{_sbindir}
cp -a tmp-install/bin/* %{buildroot}/%{_sbindir}/
popd

# Fix python shebangs
find %{buildroot}%{_datadir}/%{name}/{tools,examples} -type f -exec \
  sed -i -e '1s=^#!/usr/bin/python\([0-9.]\+\)\?$=#!%{__python3}=' \
         -e '1s=^#!/usr/bin/env python\([0-9.]\+\)\?$=#!%{__python3}=' \
         -e '1s=^#!/usr/bin/env bcc-lua$=#!/usr/bin/bcc-lua=' {} \;

# Move man pages to the right location
mkdir -p %{buildroot}%{_mandir}
mv %{buildroot}%{_datadir}/%{name}/man/* %{buildroot}%{_mandir}/

# Avoid conflict with other manpages
for i in `find %{buildroot}%{_mandir} -name "*.gz"`; do
  tname=$(basename $i)
  rename $tname %{name}-$tname $i
done
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/%{name}/examples %{buildroot}%{_docdir}/%{name}/

# Delete static libraries we don't want to ship
rm -f %{buildroot}%{_libdir}/lib%{name}*.a

# Delete old tools we don't want to ship
rm -rf %{buildroot}%{_datadir}/%{name}/tools/old/

# No tests
%check

%files
%license LICENSE.txt
%doc README.md
%{_libdir}/libbcc.so.*
%{_libdir}/libbcc_bpf.so.*

%files devel
%{_libdir}/libbcc.so
%{_libdir}/libbcc_bpf.so
%{_libdir}/pkgconfig/libbcc.pc
%{_includedir}/bcc/

%files -n python-bcc
%{python3_sitelib}/bcc*

%files doc
%dir %{_docdir}/bcc
%doc %{_docdir}/bcc/examples/

%files tools
%dir %{_datadir}/bcc
%{_datadir}/bcc/tools/
%{_datadir}/bcc/introspection/
%{_mandir}/man8/*

%files lua
%{_bindir}/bcc-lua

%files -n libbpf-tools
%{_sbindir}/bpf-*

%changelog
%autochangelog
