# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global OBCMake_version 0.3.12

Name:           libsquish
Version:        1.15.1.4
Release:        %autorelease
Summary:        Library for compressing images with the DXT/S3TC standard
License:        MIT
URL:            https://github.com/oblivioncth/libsquish
#!RemoteAsset:  sha256:8ebe37feddfc4e640541dce6a09d6144eae4606ac0dc1648e8f225d002c9531b
Source:         https://github.com/oblivioncth/libsquish/archive/refs/tags/v%{version}.tar.gz
#!RemoteAsset:  sha256:8dbdbcd052b04c2ccf03d6c6578a65e75ef2187afb48059930e43fe6d92622da
Source1:        https://github.com/oblivioncth/OBCMake/archive/refs/tags/v%{OBCMake_version}.tar.gz
BuildSystem:    cmake

BuildRequires:  cmake

BuildOption(conf):  -DNO_VERBOSE_VERSION=ON
BuildOption(conf):  -DBUILD_SHARED_LIBS=ON
BuildOption(conf):  -DFETCHCONTENT_SOURCE_DIR_OBCMAKE=$PWD/OBCmake-%{OBCMake_version}

%description
Library for compressing images with the DXT/S3TC standard.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep -a
%autosetup -p1
tar -xf %{SOURCE1} -C .

%install -a
rm -f %{buildroot}%{_prefix}/LICENSE
rm -f %{buildroot}%{_prefix}/README.md
mkdir -p %{buildroot}%{_libdir}/cmake/libsquish
mv %{buildroot}%{_prefix}/cmake/* %{buildroot}%{_libdir}/cmake/libsquish/
rmdir %{buildroot}%{_prefix}/cmake

%files
%doc README.md
%license LICENSE
%{_libdir}/libsquish.so.*

%files devel
%{_includedir}/squish/
%{_libdir}/libsquish.so
%{_libdir}/cmake/libsquish/

%changelog
%autochangelog
