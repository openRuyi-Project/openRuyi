# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           onnx-optimizer
Version:        0.4.2
Release:        %autorelease
Summary:        ONNX graph optimizer library
License:        Apache-2.0
URL:            https://github.com/onnx/optimizer
VCS:            git:https://github.com/onnx/optimizer
#!RemoteAsset:  sha256:d3509b3dfab5d8a5bc97685f8b2d7a6dd46adeefc09387ad6b2cce0c3bd698cc
Source0:        https://github.com/onnx/optimizer/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    cmake

# Use system ONNX and package shared libraries.
Patch2000:      2000-cmake-use-system-onnx-and-shared-libraries.patch

BuildOption(conf):  -DONNX_OPT_USE_SYSTEM_ONNX=ON
BuildOption(conf):  -DONNX_OPT_USE_SYSTEM_PROTOBUF=ON
BuildOption(conf):  -DONNX_BUILD_PYTHON=OFF
BuildOption(conf):  -DONNX_BUILD_TESTS=OFF
BuildOption(conf):  -DBUILD_SHARED_LIBS=ON
BuildOption(conf):  -DCMAKE_INSTALL_LIBDIR=%{_lib}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  onnx-devel
BuildRequires:  pkgconfig(protobuf)

%description
ONNX Optimizer provides a C++ library for performing optimization passes on
ONNX graphs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       onnx-devel%{?_isa}

%description    devel
Development files for %{name}.

%prep
%autosetup -p1 -n optimizer-%{version}

%check
cat > onnx-optimizer-smoke.cc <<'EOF_SMOKE'
#include <onnxoptimizer/optimize.h>

int main() {
  return 0;
}
EOF_SMOKE
%{__cxx} %{build_cxxflags} -DONNX_ML=1 -DONNX_NAMESPACE=onnx \
  -I%{buildroot}%{_includedir} \
  onnx-optimizer-smoke.cc -L%{buildroot}%{_libdir} \
  -Wl,-rpath,%{buildroot}%{_libdir} -lonnx_optimizer \
  -o onnx-optimizer-smoke
LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH} \
  ./onnx-optimizer-smoke

%files
%doc README.md
%license LICENSE
%{_libdir}/libonnx_optimizer.so.*
%{_libdir}/libonnx_optimizer_c_api.so.*

%files devel
%{_includedir}/onnxoptimizer/
%{_libdir}/libonnx_optimizer.so
%{_libdir}/libonnx_optimizer_c_api.so
%{_libdir}/cmake/ONNXOptimizer/

%changelog
%autochangelog
