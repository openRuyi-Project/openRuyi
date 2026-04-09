# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           perks
%define go_import_path  github.com/beorn7/perks

Name:           go-github-beorn7-perks
Version:        1.0.1
Release:        %autorelease
Summary:        Effective Computation of Things
License:        MIT
URL:            https://github.com/beorn7/perks
#!RemoteAsset
Source0:        https://github.com/beorn7/perks/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}
BuildOption(check):  -vet=off

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/beorn7/perks) = %{version}

%description
Perks contains the Go package quantile that computes approximate
quantiles over an unbounded data stream within low memory and CPU
bounds.

For more information and examples, see:
(http://godoc.org/github.com/bmizerany/perks)

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
