# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           flatbuffers
Version:        25.12.19
Release:        %autorelease
Summary:        Memory efficient serialization library
License:        Apache-2.0
URL:            https://github.com/google/flatbuffers
#!RemoteAsset:  sha256:f81c3162b1046fe8b84b9a0dbdd383e24fdbcf88583b9cb6028f90d04d90696a
Source0:        https://github.com/google/flatbuffers/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DFLATBUFFERS_BUILD_SHAREDLIB=ON
BuildOption(conf):  -DFLATBUFFERS_BUILD_FLATLIB=OFF
BuildOption(conf):  -DFLATBUFFERS_BUILD_FLATC=ON
BuildOption(conf):  -DFLATBUFFERS_BUILD_TESTS=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  pyproject-rpm-macros

%description
FlatBuffers is a cross platform serialization library architected for maximum
memory efficiency.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development headers and libraries for flatbuffers.

%package     -n python-flatbuffers
Summary:        FlatBuffers serialization format for Python
BuildArch:      noarch
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       python3-%{name}
%python_provide python3-%{name}

%description -n python-flatbuffers
Python runtime library for Flatbuffers.

%prep -a
%generate_buildrequires
cd python
%pyproject_buildrequires

%build -a
export VERSION='%{version}'
cd python
%pyproject_wheel

%install -a
cd python
%pyproject_install
%pyproject_save_files flatbuffers

%files
%license LICENSE
%{_libdir}/libflatbuffers.so.*
%{_bindir}/flatc

%files devel
%{_includedir}/flatbuffers/
%{_libdir}/libflatbuffers.so
%{_libdir}/cmake/flatbuffers/
%{_libdir}/pkgconfig/flatbuffers.pc

%files -n python-flatbuffers -f %{pyproject_files}
%license LICENSE

%changelog
%{?autochangelog}
