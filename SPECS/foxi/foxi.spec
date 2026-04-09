# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit0 c278588e34e535f0bb8f00df3880d26928038cad
%global date0 20260211
%global shortcommit0 c278588

# Use pytorch's toolchain
%global toolchain clang

Name:           foxi
Version:        0+git%{date0}.%{shortcommit0}
Release:        %autorelease
Summary:        ONNXIFI with Facebook Extension
License:        MIT
URL:            https://github.com/houseroad/foxi
#!RemoteAsset
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
BuildSystem:    cmake

# https://github.com/houseroad/foxi/pull/25
Patch0:         0001-Fix-signatures-of-functions.patch

BuildOption(conf):  -DONNX_USE_LITE_PROTO=OFF

BuildRequires:  cmake
BuildRequires:  clang

%description
%{summary}

%package        devel
Summary:        Headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
%{summary}

%prep -a
# Change static library to shared
sed -i -e 's/foxi_loader STATIC/foxi_loader SHARED/' CMakeLists.txt
# Disable hidden so shared foxi_loader will find onnxifi_load
sed -i -e 's/__ELF_/__NO_ELF_DISABLING_HIDDEN__/' foxi/onnxifi_loader.h
# Fix the destination lib
sed -i -e 's/DESTINATION lib/DESTINATION lib64/' CMakeLists.txt
# Just install libfoxi_loader
sed -i -e 's/foxi foxi_dummy foxi_loader/foxi_loader/' CMakeLists.txt
# version *.so
echo "set_target_properties(foxi_loader PROPERTIES SOVERSION \"1.4.1\")" >> CMakeLists.txt

# For CMake 4
sed -i 's@cmake_minimum_required(VERSION 3.1@cmake_minimum_required(VERSION 3.5@' CMakeLists.txt

%files
%license LICENSE
%exclude %{_libdir}/libfoxi.so
%{_libdir}/libfoxi_loader.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/libfoxi_loader.so

%changelog
%autochangelog
