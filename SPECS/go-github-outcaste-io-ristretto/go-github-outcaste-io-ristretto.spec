# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           ristretto
%define go_import_path  github.com/outcaste-io/ristretto

Name:           go-github-outcaste-io-ristretto
Version:        0.2.3
Release:        %autorelease
Summary:        High-performance concurrent cache library for Go
License:        Apache-2.0
URL:            https://github.com/outcaste-io/ristretto
#!RemoteAsset:  sha256:8ec2299cb3c45a6f896d005a59797a2f6a5775735a843407224c979151ea0428
Source0:        https://github.com/outcaste-io/ristretto/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/dgryski/go-farm)
BuildRequires:  go(github.com/dustin/go-humanize)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(go.uber.org/atomic)
BuildRequires:  go(golang.org/x/sys)

Provides:       go(%{go_import_path}) = %{version}

Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/dgryski/go-farm)
Requires:       go(github.com/dustin/go-humanize)
Requires:       go(github.com/pkg/errors)
Requires:       go(go.uber.org/atomic)
Requires:       go(golang.org/x/sys)

%description
Ristretto is a concurrent, fixed-size cache library focused on high throughput
and a high cache hit ratio.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
