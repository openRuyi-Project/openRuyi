# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname unicorn

Name:           %{srcname}
Version:        2.1.4
Release:        %autorelease
Summary:        Lightweight multi-platform, multi-architecture CPU emulator framework
License:        GPL-2.0-only AND LGPL-2.1-or-later AND MIT AND BSD-2-Clause AND BSD-3-Clause
URL:            https://www.unicorn-engine.org/
VCS:            git:https://github.com/unicorn-engine/unicorn/
#!RemoteAsset:  sha256:ea8863f095a0136388694e5a6063afd9bb7650e30243dd6251af59c5ce5601f4
Source0:        https://github.com/unicorn-engine/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildSystem:    cmake

%ifarch riscv64
# ARM/ARM64 mem hook tests are unstable on riscv64 hosts now.
BuildOption(check):  --output-on-failure -E "(test_arm|test_arm64)"
%else
BuildOption(check):  --output-on-failure
%endif

BuildRequires:  cmake
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(pip)
BuildRequires:  pkgconfig(python3)

%description
Unicorn is a lightweight multi-platform, multi-architecture CPU emulator
framework.

%package        devel
Summary:        Files needed to develop applications using unicorn
Requires:       %{name} = %{version}-%{release}

%description    devel
This package provides the libraries, include files, and other resources
needed for developing applications using unicorn.

%package     -n python-%{srcname}
Summary:        %{summary}
Requires:       %{name} = %{version}-%{release}
Requires:       python3dist(setuptools)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description -n python-%{srcname}
The unicorn-python3 package contains python3 bindings for unicorn.

%prep -a
%generate_buildrequires
pushd bindings/python
%pyproject_buildrequires
popd

%build -a
pushd bindings/python
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
popd

%install -a
pushd bindings/python
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
popd
rm $RPM_BUILD_ROOT%{_libdir}/libunicorn.a
rm $RPM_BUILD_ROOT%{_libdir}/unicorn.o

%files
%doc AUTHORS.TXT CREDITS.TXT README.md
%license COPYING
%{_libdir}/libunicorn.so.2

%files devel
%{_libdir}/libunicorn.so
%{_libdir}/pkgconfig/unicorn.pc
%{_includedir}/unicorn/

%files -n python-%{srcname}
%{python3_sitearch}/%{srcname}-*.dist-info/
%{python3_sitearch}/%{srcname}/

%changelog
%autochangelog
