# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           vapoursynth
Version:        73
Release:        %autorelease
Summary:        Video processing framework with simplicity in mind
License:        LGPL-2.1-only
URL:            https://github.com/vapoursynth/vapoursynth
#!RemoteAsset:  sha256:1bb8ffe31348eaf46d8f541b138f0136d10edaef0c130c1e5a13aa4a4b057280
Source0:        https://github.com/vapoursynth/vapoursynth/archive/refs/tags/R%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-core
BuildOption(conf):  --enable-vsscript
BuildOption(conf):  --enable-vspipe
BuildOption(conf):  --enable-python-module
%ifarch x86_64
BuildOption(conf):  --enable-x86-asm
%endif

%ifarch x86_64
BuildRequires:  nasm
%endif
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc-c++
BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(zimg)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(pytest)

%description
VapourSynth is an application for video manipulation. Or a plugin. Or a library.
It has a core library written in C++ and a Python module to allow video scripts
to be created.

%package     -n python-%{name}
Summary:        Python interface for VapourSynth
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       python3-%{name}
%python_provide python3-%{name}

%description -n python-%{name}
Python interface for VapourSynth/VSScript.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.

%conf -p
autoreconf -vif

%generate_buildrequires
%pyproject_buildrequires

%build -a
ln -sf .libs build
%pyproject_wheel

%install -a
%pyproject_install
%pyproject_save_files -l %{name}

%files
%license COPYING.LESSER
%doc ChangeLog
%{_bindir}/vspipe
%{_libdir}/libvapoursynth-script.so.*

%files devel
%{_includedir}/vapoursynth/
%{_libdir}/libvapoursynth.so
%{_libdir}/libvapoursynth-script.so
%{_libdir}/pkgconfig/vapoursynth.pc
%{_libdir}/pkgconfig/vapoursynth-script.pc

%files -n python-vapoursynth -f %{pyproject_files}
%{python3_sitearch}/vapoursynth.so
%{python3_sitearch}/cython/
%{python3_sitearch}/vsscript/

%changelog
%autochangelog
