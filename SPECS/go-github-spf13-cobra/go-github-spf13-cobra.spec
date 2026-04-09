# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           cobra
%define go_import_path  github.com/spf13/cobra

Name:           go-github-spf13-cobra
Version:        1.10.2
Release:        %autorelease
Summary:        A Commander for modern Go CLI interactions
License:        Apache-2.0
URL:            https://github.com/spf13/cobra
#!RemoteAsset
Source0:        https://github.com/spf13/cobra/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/cpuguy83/go-md2man/v2)
BuildRequires:  go(github.com/spf13/pflag)
BuildRequires:  go(go.yaml.in/yaml/v3)

Provides:       go(github.com/spf13/cobra) = %{version}

Requires:       go(github.com/cpuguy83/go-md2man/v2)
Requires:       go(github.com/spf13/pflag)
Requires:       go(github.com/spf13/viper)
Requires:       go(go.yaml.in/yaml/v3)

%description
Cobra is a library for creating powerful modern CLI applications.

Cobra is used in many Go projects such as Kubernetes
(https://kubernetes.io/), Hugo (https://gohugo.io), and GitHub CLI
(https://github.com/cli/cli) to name a few. This list
(/site/content/projects_using_cobra.md) contains a more extensive list
of projects using Cobra.

%prep
%autosetup -n %{_name}-%{version}

%files
%license LICENSE*
%doc README*
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
