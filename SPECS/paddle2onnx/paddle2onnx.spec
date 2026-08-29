# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           paddle2onnx
Version:        1.0.0
Release:        %autorelease
Summary:        PaddlePaddle to ONNX model converter library
License:        Apache-2.0
URL:            https://github.com/PaddlePaddle/Paddle2ONNX
VCS:            git:https://github.com/PaddlePaddle/Paddle2ONNX.git
# PaddlePaddle 3.3.x uses the IsExportable C++ API that was removed from newer
# Paddle2ONNX releases, so package the latest compatible stable release.
#!RemoteAsset:  sha256:68e8e035828f684b0fc81b6d14a876e6c7961b419dce7ae5f22e94418c51b985
Source0:        https://github.com/PaddlePaddle/Paddle2ONNX/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    cmake

# Use system ONNX, ONNX Optimizer, protobuf, and the distribution libdir.
Patch2000:      2000-cmake-use-system-protobuf-and-libdir.patch

BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5
BuildOption(conf):  -DBUILD_PADDLE2ONNX_EXE=OFF
BuildOption(conf):  -DBUILD_PADDLE2ONNX_PYTHON=OFF
BuildOption(conf):  -DWITH_STATIC=OFF
BuildOption(conf):  -DCMAKE_INSTALL_LIBDIR=%{_lib}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  onnx-devel
BuildRequires:  onnx-optimizer-devel
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(python3)

%description
Paddle2ONNX provides a C++ library for converting PaddlePaddle models to ONNX.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       onnx-devel%{?_isa}
Requires:       onnx-optimizer-devel%{?_isa}

%description    devel
Development files for %{name}.

%prep
%autosetup -p1 -n Paddle2ONNX-%{version}

%install -a
# libpaddle2onnx links this internal shared library; keep it in the main
# package because upstream does not install it.
install -p -m 0755 %{_build}/paddle2onnx/proto/libp2o_paddle_proto.so \
  %{buildroot}%{_libdir}/libp2o_paddle_proto.so

%files
%license LICENSE
%{_libdir}/libp2o_paddle_proto.so
%{_libdir}/libpaddle2onnx.so.*

%files devel
%{_includedir}/paddle2onnx/
%{_libdir}/libpaddle2onnx.so

%changelog
%autochangelog
