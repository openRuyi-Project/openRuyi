# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           jsonnet
Version:        0.21.0
Release:        %autorelease
Summary:        A data templating language based on JSON
License:        Apache-2.0 AND MIT AND CC0-1.0
URL:            https://github.com/google/jsonnet
#!RemoteAsset:  sha256:a12ebca72e43e7061ffe4ef910e572b95edd7778a543d6bf85f6355bd290300e
Source0:        https://github.com/google/jsonnet/archive/refs/tags/v%{version}.tar.gz
Source1:        jsonnet.1
Source2:        jsonnetfmt.1
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_TESTS:BOOL=OFF
BuildOption(conf):  -DBUILD_SHARED_BINARIES:BOOL=ON
BuildOption(conf):  -DBUILD_STATIC_LIBS:BOOL=OFF
BuildOption(conf):  -DUSE_SYSTEM_JSON:BOOL=ON
BuildOption(conf):  -DBUILD_STATIC_LIBS=OFF
BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM:STRING=3.5

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(setuptools)
BuildRequires:  bash
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  nlohmann-json
BuildRequires:  python3dist(pip)

%description
A data templating language for app and tool developers based on JSON.

%package     -n python-%{name}
Summary:        %{name} Bindings for Python
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       python3-%{name} = %{version}-%{release}
%python_provide python3-%{name}

%description -n python-%{name}
Python bindings for the jsonnet data templating language.

%package        devel
Summary:        Development Headers for %{name}
License:        Apache-2.0
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development headers for the jsonnet data templating language.

%generate_buildrequires -a
%pyproject_buildrequires

%build -a
# make python binding
%{__cp} %{_vpath_builddir}/libjsonnet*.so .
%pyproject_wheel

%install -a
%pyproject_install
%pyproject_save_files _jsonnet

install -d -m 755 '%{buildroot}%{_mandir}/man1'
install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 '%{SOURCE1}' '%{SOURCE2}'

%files
%license LICENSE
%doc README.md
%doc CONTRIBUTING
%doc doc
%doc examples
%{_bindir}/jsonnet
%{_bindir}/jsonnetfmt
%{_mandir}/man1/jsonnet.1*
%{_mandir}/man1/jsonnetfmt.1*
%{_libdir}/libjsonnet.so.*
%{_libdir}/libjsonnet++.so.*

%files devel
%{_includedir}/libjsonnet*
%{_libdir}/libjsonnet.so
%{_libdir}/libjsonnet++.so

%files -n python-%{name} -f %{pyproject_files}

%changelog
%autochangelog
