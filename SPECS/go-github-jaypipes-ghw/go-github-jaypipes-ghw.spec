# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ghw
%define go_import_path  github.com/jaypipes/ghw

Name:           go-github-jaypipes-ghw
Version:        0.11.0
Release:        %autorelease
Summary:        Hardware discovery and inspection for Go
License:        Apache-2.0
URL:            https://github.com/jaypipes/ghw
#!RemoteAsset:  sha256:c53da6d7e087d097ade828a066821bc572f95d60247aaca7b77c521c1a347a16
Source0:        https://github.com/jaypipes/ghw/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# The host disk test requires a serial number unavailable in the OBS guest.
BuildOption(check):  -skip "^Test(Block${ghw_skip_cpu})$"

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  hwdata
BuildRequires:  go(github.com/StackExchange/wmi)
BuildRequires:  go(github.com/ghodss/yaml)
BuildRequires:  go(github.com/jaypipes/pcidb)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(howett.net/plist)

Provides:       go(github.com/jaypipes/ghw) = %{version}

Requires:       go(github.com/StackExchange/wmi)
Requires:       go(github.com/ghodss/yaml)
Requires:       go(github.com/jaypipes/pcidb)
Requires:       go(github.com/pkg/errors)
Requires:       go(howett.net/plist)

%description
Hardware discovery and inspection for Go.

%prep -a
# The optional inspection CLI adds no library API.
rm -rf cmd

%check -p
# Upstream does not populate RISC-V CPU capabilities; retain the CPU snapshot tests.
ghw_skip_cpu=
if [ "$(go env GOARCH)" = riscv64 ]; then
    ghw_skip_cpu='|CPU'
fi

%files
%doc README.md
%license COPYING
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
