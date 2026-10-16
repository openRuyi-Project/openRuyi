# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define source_version  0.13.4-1
%define _name           go-nvml
%define go_import_path  github.com/NVIDIA/go-nvml

Name:           go-github-nvidia-go-nvml
Version:        0.13.4.1
Release:        %autorelease
Summary:        Go bindings for the NVIDIA Management Library
License:        Apache-2.0
URL:            https://github.com/NVIDIA/go-nvml
#!RemoteAsset:  sha256:55ffd2c3e7aed903422279843369e3440b4a6d7c5306392cae0ece83d875e746
Source0:        https://github.com/NVIDIA/go-nvml/archive/v%{source_version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  gcc
BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.yaml.in/yaml/v3)

Provides:       go(github.com/NVIDIA/go-nvml) = %{version}
Provides:       go(github.com/NVIDIA/go-nvml/pkg/dl) = %{version}
Provides:       go(github.com/NVIDIA/go-nvml/pkg/nvml) = %{version}

Requires:       go(github.com/google/uuid)

Requires:       go(go.yaml.in/yaml/v3)

%description
This package provides Go bindings and test mocks for the NVIDIA Management
Library. The library is loaded dynamically; compiling the bindings does not
require an NVIDIA driver.

%prep -a
# Use distribution dependencies instead of the archive's vendored copies.
rm -rf vendor

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
