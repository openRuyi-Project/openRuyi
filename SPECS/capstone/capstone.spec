# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jvle <keke.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects

%global srcname capstone

Name:           %{srcname}
Version:        5.0.9
Release:        %autorelease
Summary:        A multi-platform, multi-architecture disassembly framework
License:        BSD-3-Clause
URL:            https://www.capstone-engine.org
VCS:            git:https://github.com/capstone-engine/capstone
#!RemoteAsset:  sha256:0619da31af08152600af95c481527ef6d756c0a8404fca7544a4fdf6dfc2c0f9
Source0:        https://github.com/capstone-engine/%{srcname}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    cmake

# From https://github.com/capstone-engine/capstone/commit/e17ee44a8307ea33375b4727ac4f987650bf7bed
Patch1000:      1000-V5-Fix-OOB-reads-writes-CVE-2026-55893-CVE-2026-5589.patch
# From https://github.com/capstone-engine/capstone/commit/de4b58b2e74b92296a1e181f4121c42bd65eb286
Patch1001:      1001-GHSA-5q63-4654-94v6-fail-invalid-long-instruction.patch

BuildOption(conf):  -DBUILD_SHARED_LIBS=ON
BuildOption(conf):  -DCAPSTONE_BUILD_CSTOOL=ON
BuildOption(conf):  -DCAPSTONE_BUILD_CSTEST=OFF
BuildOption(conf):  -DCAPSTONE_BUILD_TESTS=OFF

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)

%description
Capstone is a disassembly framework.
disasm engine for binary analysis and reversing in the security community.

%package        devel
Summary:        Development files to build upon libcapstone
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files to build upon libcapstone, C language only.

%package        doc
Summary:        Documentation for capstone, a disassembly framework
BuildArch:      noarch

%description    doc
Capstone is a multi-architecture disassembly framework.

%package     -n python-%{srcname}
Summary:        Python bindings for the Capstone disassembly framework
BuildArch:      noarch
Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description -n python-%{srcname}
Capstone is a multi-architecture disassembly framework.

This package contains the Capstone bindings for Python.

%build -a
cd %{_builddir}/%{name}-%{version}
pushd bindings/python
LIBCAPSTONE_PATH=../../%{_vpath_builddir} %{__python3} setup.py bdist_wheel
popd

%install -a
install -m 755 -d %{buildroot}%{_docdir}/%{name}-doc/docs
install -m 644 -t %{buildroot}%{_docdir}/%{name}-doc/docs docs/README docs/*.pdf

pushd bindings/python
%{__python3} -m pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
rm -rf %{buildroot}%{python3_sitelib}/capstone/lib
rm -rf %{buildroot}%{python3_sitelib}/capstone/include
popd

# fix pkgconfig file
sed -e '/^archive/d' -e 's|^libdir=.*|libdir=%{_libdir}|' \
    -i %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

# Delete static libraries we don't want to ship
rm -f %{buildroot}%{_libdir}/lib%{name}*.a

%fdupes %{buildroot}

%files
%license LICENSE*.TXT
%{_bindir}/cstool
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/capstone.pc
%{_libdir}/cmake/%{srcname}/

%files -n python-%{srcname}
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-*.dist-info/

%files doc
%license LICENSE*.TXT
%doc ChangeLog README.md
%{_docdir}/%{srcname}-doc/docs/

%changelog
%autochangelog
