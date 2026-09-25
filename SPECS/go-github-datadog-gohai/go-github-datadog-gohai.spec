# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           gohai
%define go_import_path  github.com/DataDog/gohai
%define commit_id       4316413895ee2c3c35755fb3161f12bafe122b62

Name:           gohai
Version:        0+git20260817.4316413
Release:        %autorelease
Summary:        System information collector for Go
License:        MIT
URL:            https://github.com/DataDog/gohai
#!RemoteAsset:  sha256:a1723060f7ef4787e1edc631d8b88b25f527aa0044ad195f1f3d5c9ab9e49e84
Source0:        https://github.com/DataDog/gohai/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golang

# Commit archives extract with the full hash instead of the RPM version.
BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cihub/seelog)
BuildRequires:  go(github.com/shirou/gopsutil/v3)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/sys)

%description
Gohai is a command-line tool for collecting system information.

%package     -n go-github-datadog-gohai
Summary:        System information collector library for Go
BuildArch:      noarch
Provides:       go(%{go_import_path}) = %{version}
Provides:       go(%{go_import_path}/cpu) = %{version}
Provides:       go(%{go_import_path}/filesystem) = %{version}
Provides:       go(%{go_import_path}/memory) = %{version}
Provides:       go(%{go_import_path}/network) = %{version}
Provides:       go(%{go_import_path}/platform) = %{version}
Provides:       go(%{go_import_path}/processes) = %{version}
Provides:       go(%{go_import_path}/utils) = %{version}

Requires:       go(github.com/cihub/seelog)
Requires:       go(github.com/shirou/gopsutil/v3)
Requires:       go(golang.org/x/sys)

%description -n go-github-datadog-gohai
This package contains the reusable Go source from the Gohai repository.

%install -a
# The command is already installed; keep its architecture-dependent build
# artifact out of the noarch source subpackage before copying the source tree.
rm -f %{_name}
%buildsystem_golangmodules_install

%check -p
# RISC-V lacks the x86 CPU fields asserted by the root serialization test.
if [ "%{_target_cpu}" = riscv64 ]; then
    export GOFLAGS="${GOFLAGS:+${GOFLAGS} }-skip=TestGohaiSerialization"
fi

%files
%doc README.md
%license LICENSE
%{_bindir}/%{_name}

%files -n go-github-datadog-gohai
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
