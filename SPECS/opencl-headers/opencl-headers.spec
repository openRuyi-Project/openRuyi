# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global clhpp_version 2026.05.29
%global clhpp_builddir OpenCL-CLHPP-%{clhpp_version}

Name:           opencl-headers
Version:        2026.05.29
Release:        %autorelease
Summary:        OpenCL (Open Computing Language) header files
License:        Apache-2.0
URL:            https://github.com/KhronosGroup/OpenCL-Headers
VCS:            git:https://github.com/KhronosGroup/OpenCL-Headers.git
#!RemoteAsset:  sha256:d9e6c48357de5002da11ce45de600e0c3ffe6ab4f628a3b9fe2b38603161658a
Source0:        https://github.com/KhronosGroup/OpenCL-Headers/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
#!RemoteAsset:  sha256:fafb4fd202d113992c009d46e6358e70076167e62a5baeb377fe813033a2655e
Source1:        https://github.com/KhronosGroup/OpenCL-CLHPP/archive/refs/tags/v%{clhpp_version}/opencl-clhpp-%{clhpp_version}.tar.gz
BuildArch:      noarch
BuildSystem:    cmake

BuildOption(prep):  -a 1
BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
OpenCL (Open Computing Language) header files.

%conf -a
# Use the Headers build-tree package without installing it first.
cmake -S %{clhpp_builddir} -B build-clhpp \
    -DOpenCLHeaders_DIR="$PWD/%{__cmake_builddir}/OpenCLHeaders" \
    -DBUILD_DOCS=OFF \
    -DBUILD_EXAMPLES=OFF \
    -DBUILD_TESTING=OFF

%build -a
cmake --build build-clhpp

%install -a
cmake --install build-clhpp --prefix "%{buildroot}/%{_prefix}"

# We're not interested in Direct3D things
rm -vf %{buildroot}%{_includedir}/CL/cl_{dx9,d3d}*

%files
%license LICENSE
%license %{clhpp_builddir}/LICENSE.txt
%dir %{_includedir}/CL
%{_includedir}/CL/cl2.hpp
%{_includedir}/CL/cl_egl.h
%{_includedir}/CL/cl_ext.h
%{_includedir}/CL/cl_ext_intel.h
%{_includedir}/CL/cl_function_types.h
%{_includedir}/CL/cl_gl_ext.h
%{_includedir}/CL/cl_gl.h
%{_includedir}/CL/cl.h
%{_includedir}/CL/cl_half.h
%{_includedir}/CL/cl_icd.h
%{_includedir}/CL/cl_layer.h
%{_includedir}/CL/cl_platform.h
%{_includedir}/CL/cl_va_api_media_sharing_intel.h
%{_includedir}/CL/cl_version.h
%{_includedir}/CL/opencl.h
%{_includedir}/CL/opencl.hpp
%{_datadir}/pkgconfig/OpenCL-Headers.pc
%{_datadir}/pkgconfig/OpenCL-CLHPP.pc
%{_datadir}/cmake/OpenCLHeaders/
%{_datadir}/cmake/OpenCLHeadersCpp/

%changelog
%autochangelog
