# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-metadata
%define go_import_path  github.com/digitalocean/go-metadata
%define commit_id       e3650a3df44b875c97f6df0dc28f9ca11d23cc4d

Name:           go-github-digitalocean-go-metadata
Version:        0+git20260906.e3650a3
Release:        %autorelease
Summary:        Go client for the DigitalOcean metadata API
License:        MIT
URL:            https://github.com/digitalocean/go-metadata
VCS:            git:https://github.com/digitalocean/go-metadata.git
#!RemoteAsset:  sha256:996a528c660a0feb069cc385bd48696092fa8a7a65cb7e86642629a6736de23a
Source0:        https://github.com/digitalocean/go-metadata/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildRequires:  go
BuildRequires:  go-rpm-macros

Provides:       go(%{go_import_path}) = %{version}

%description
This library queries the DigitalOcean metadata API for information about
a Droplet, including its network configuration, region, and user data.

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
