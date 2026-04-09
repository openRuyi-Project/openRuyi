# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit       b4b77d1006e764fb5cc42597d17d2b110211c2d1
%global shortcommit  %(c=%{commit}; echo ${c:0:7})

# Building from source requires libnop, which is usually not available as a system package,
# so it needs to be installed manually.
%global libnop_commit 35e800d81f28c632956c5a592e3cbe8085ecd430

Name:           tensorpipe
Version:        0+git20251218.%{shortcommit}
Release:        %autorelease
Summary:        A tensor-aware channel for transferring rich objects
License:        BSD-3-Clause
URL:            https://github.com/pytorch/tensorpipe
#!RemoteAsset:  sha256:adeb3c79da0972034c7fea0df277108778ae210e1f05275988dd92907a3b05c8
Source0:        https://github.com/pytorch/tensorpipe/archive/%{commit}/tensorpipe-%{commit}.tar.gz
#!RemoteAsset:  sha256:c377bfc07e0029bcd2da23597b9dc668c2450508f57b612fdae0542e097a4f63
Source1:        https://github.com/google/libnop/archive/%{libnop_commit}/libnop-%{libnop_commit}.tar.gz
BuildSystem:    cmake

BuildOption(prep):  -a1
BuildOption(conf):  -DTENSORPIPE_BUILD_TESTS=OFF

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(pybind11)

%description
The TensorPipe project provides a tensor-aware channel to transfer rich objects
from one process to another while using the fastest transport for the tensors
contained therein (e.g., CUDA device-to-device copy).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for tensorpipe.

%prep -a
mv libnop-%{libnop_commit}/* third_party/libnop

%files
%license LICENSE.txt
%doc README.md
%{_libdir}/libtensorpipe.so

%files devel
%{_includedir}/tensorpipe/
%{_datadir}/cmake/Tensorpipe/

%changelog
%autochangelog
