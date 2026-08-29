# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           dtc
Version:        1.7.2
Release:        %autorelease
Summary:        Device Tree Compiler
License:        GPL-2.0-or-later
URL:            https://devicetree.org/
VCS:            git:https://github.com/dgibson/dtc
#!RemoteAsset:  sha256:92d8ca769805ae1f176204230438fe52808f4e1c7944053c9eec0e649b237539
Source0:        https://www.kernel.org/pub/software/utils/%{name}/%{name}-%{version}.tar.xz
#!RemoteAsset:  sha256:76929711ac4c53bd283619037c3d853d4e97bdbfd5a793a09e11698824b7032e
Source1:        https://www.kernel.org/pub/software/utils/%{name}/%{name}-%{version}.tar.sign
BuildSystem:    autotools

# https://github.com/dgibson/dtc/issues/163
Patch0:         0001-Test-failure-with-newer-glibc.patch
# From https://github.com/dgibson/dtc/commit/9a1c801a1a3c102bf95c5339c9e985b26b823a21
Patch1:         0002-fix-discarded-const-qualifiers.patch
# https://qemu.googlesource.com/dtc/+/9a969f3b70b07bbf1c9df44a38d7f8d1d3a6e2a5
Patch1000:      1000-backport-pylibfdt-libfdt.i-fix-backwards-compatibility-of-return-values.patch

BuildOption(install):  V=1 DESTDIR=%{buildroot} PREFIX=%{buildroot}/%{_prefix}
BuildOption(install):  LIBDIR=%{_libdir} BINDIR=%{_bindir} INCLUDEDIR=%{_includedir}

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  swig
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(wheel)
Provides:       libfdt%{?_isa} = %{version}-%{release}
Obsoletes:      libfdt < %{version}-%{release}

%description
The devicetree is a data structure for describing hardware. Rather than hard coding
every detail of a device into an operating system, many aspects of the hardware can
be described in a data structure that is passed to the operating system at boot time.
The devicetree is used by OpenFirmware, OpenPOWER Abstraction Layer (OPAL), Power
Architecture Platform Requirements (PAPR) and in the standalone Flattened Device
Tree (FDT) form.

%package        devel
Summary:        Development headers for device tree library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       libfdt-static%{?_isa} = %{version}-%{release}
Provides:       libfdt-devel%{?_isa} = %{version}-%{release}
Obsoletes:      libfdt-static < %{version}-%{release}
Obsoletes:      libfdt-devel < %{version}-%{release}

%description    devel
This package provides development files for dtc.

%package     -n python-libfdt
Summary:        Python bindings for device tree library
%{?python_provide:%python_provide python3-libfdt}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n python-libfdt
This package provides python bindings for libfdt

# no configure
%conf

%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%install -p
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%check -p
%define _smp_mflags -j1
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%files
%license GPL README.license
%doc Documentation/manual.txt
%{_bindir}/*
%{_libdir}/libfdt.so.*

%files devel
%{_libdir}/libfdt.so
%{_includedir}/*
%{_libdir}/libfdt.a

%files -n python-libfdt
%{python3_sitearch}/*

%changelog
%autochangelog
