# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           docker-credential-helpers
%define go_import_path  github.com/docker/docker-credential-helpers
%define go_test_include %{shrink:
    %{go_import_path}/client
    %{go_import_path}/credentials
}

Name:           go-github-docker-docker-credential-helpers
Version:        0.6.3
Release:        %autorelease
Summary:        Go library for docker-credential-helpers
License:        MIT
URL:            https://github.com/docker/docker-credential-helpers
VCS:            git:https://github.com/docker/docker-credential-helpers.git
#!RemoteAsset:  sha256:441684cf1d2434aa1024aa2f8455e11502c44858e93ea171b19caa656dd2b2e2
Source0:        https://github.com/docker/docker-credential-helpers/archive/v0.6.3.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n docker-credential-helpers-0.6.3

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(github.com/docker/docker-credential-helpers) = %{version}

%description
This package provides the github.com/docker/docker-credential-helpers Go module source.

%prep -a
# Do not install a nested vendor tree into the shared Go source path.
rm -rf vendor

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
