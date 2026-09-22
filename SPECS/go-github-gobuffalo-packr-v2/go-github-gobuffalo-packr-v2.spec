# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           packr
%define go_import_path  github.com/gobuffalo/packr/v2
%define go_test_include %{go_import_path}

Name:           go-github-gobuffalo-packr-v2
Version:        2.7.1
Release:        %autorelease
Summary:        NOTICE: Please consider migrating your projects to
License:        MIT
URL:            https://github.com/gobuffalo/packr
VCS:            git:https://github.com/gobuffalo/packr.git
#!RemoteAsset:  sha256:842bc86dfb34c1ff8d1cc1c12fb46cf30ad279eec17ecef8b122c151cfc16b85
Source0:        https://github.com/gobuffalo/packr/archive/v2.7.1.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n packr-2.7.1

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/gobuffalo/envy)
BuildRequires:  go(github.com/gobuffalo/logger)
BuildRequires:  go(github.com/gobuffalo/packd)
BuildRequires:  go(github.com/karrick/godirwalk)
BuildRequires:  go(github.com/rogpeppe/go-internal)
BuildRequires:  go(github.com/sirupsen/logrus)
BuildRequires:  go(github.com/spf13/cobra)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/tools)

Provides:       go(github.com/gobuffalo/packr/v2) = %{version}

Requires:       go(github.com/gobuffalo/envy)
Requires:       go(github.com/gobuffalo/logger)
Requires:       go(github.com/gobuffalo/packd)
Requires:       go(github.com/karrick/godirwalk)
Requires:       go(github.com/rogpeppe/go-internal)
Requires:       go(github.com/sirupsen/logrus)
Requires:       go(github.com/spf13/cobra)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/tools)

%description
This package provides the github.com/gobuffalo/packr/v2 Go module source.

%install
# The tagged archive keeps the v2 module below the legacy v1 source tree.
pushd v2
%buildsystem_golangmodules_install
popd

%check
pushd v2
%buildsystem_golangmodules_check
popd

%files
%doc v2/README.md
%license v2/LICENSE.txt
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
