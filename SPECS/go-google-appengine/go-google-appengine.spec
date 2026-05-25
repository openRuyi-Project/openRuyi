# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           appengine
%define go_import_path  google.golang.org/appengine

Name:           go-google-appengine
Version:        2.0.6
Release:        %autorelease
Summary:        Go library for google.golang.org/appengine
License:        Apache-2.0
URL:            https://github.com/golang/appengine
#!RemoteAsset:  sha256:c6dff11b0af82470f79fd4a017de7b09574bfc73a0af1e65589357d22ea93f14
Source0:        https://github.com/golang/appengine/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n appengine-2.0.6

BuildRequires:  go
BuildRequires:  go(github.com/golang/protobuf)
BuildRequires:  go(golang.org/x/net/context)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go-rpm-macros

Provides:       go(google.golang.org/appengine) = %{version}
Provides:       go(google.golang.org/appengine/aetest) = %{version}
Provides:       go(google.golang.org/appengine/blobstore) = %{version}
Provides:       go(google.golang.org/appengine/capability) = %{version}
Provides:       go(google.golang.org/appengine/channel) = %{version}
Provides:       go(google.golang.org/appengine/cloudsql) = %{version}
Provides:       go(google.golang.org/appengine/datastore) = %{version}
Provides:       go(google.golang.org/appengine/datastore/internal/cloudkey) = %{version}
Provides:       go(google.golang.org/appengine/datastore/internal/cloudpb) = %{version}
Provides:       go(google.golang.org/appengine/delay) = %{version}
Provides:       go(google.golang.org/appengine/file) = %{version}
Provides:       go(google.golang.org/appengine/image) = %{version}
Provides:       go(google.golang.org/appengine/internal) = %{version}
Provides:       go(google.golang.org/appengine/internal/aetesting) = %{version}
Provides:       go(google.golang.org/appengine/internal/app_identity) = %{version}
Provides:       go(google.golang.org/appengine/internal/base) = %{version}
Provides:       go(google.golang.org/appengine/internal/blobstore) = %{version}
Provides:       go(google.golang.org/appengine/internal/capability) = %{version}
Provides:       go(google.golang.org/appengine/internal/channel) = %{version}
Provides:       go(google.golang.org/appengine/internal/datastore) = %{version}
Provides:       go(google.golang.org/appengine/internal/image) = %{version}
Provides:       go(google.golang.org/appengine/internal/log) = %{version}
Provides:       go(google.golang.org/appengine/internal/mail) = %{version}
Provides:       go(google.golang.org/appengine/internal/memcache) = %{version}
Provides:       go(google.golang.org/appengine/internal/modules) = %{version}
Provides:       go(google.golang.org/appengine/internal/remote_api) = %{version}
Provides:       go(google.golang.org/appengine/internal/search) = %{version}
Provides:       go(google.golang.org/appengine/internal/socket) = %{version}
Provides:       go(google.golang.org/appengine/internal/system) = %{version}
Provides:       go(google.golang.org/appengine/internal/taskqueue) = %{version}
Provides:       go(google.golang.org/appengine/internal/urlfetch) = %{version}
Provides:       go(google.golang.org/appengine/internal/user) = %{version}
Provides:       go(google.golang.org/appengine/internal/xmpp) = %{version}
Provides:       go(google.golang.org/appengine/log) = %{version}
Provides:       go(google.golang.org/appengine/mail) = %{version}
Provides:       go(google.golang.org/appengine/memcache) = %{version}
Provides:       go(google.golang.org/appengine/module) = %{version}
Provides:       go(google.golang.org/appengine/remote_api) = %{version}
Provides:       go(google.golang.org/appengine/runtime) = %{version}
Provides:       go(google.golang.org/appengine/search) = %{version}
Provides:       go(google.golang.org/appengine/socket) = %{version}
Provides:       go(google.golang.org/appengine/taskqueue) = %{version}
Provides:       go(google.golang.org/appengine/urlfetch) = %{version}
Provides:       go(google.golang.org/appengine/user) = %{version}
Provides:       go(google.golang.org/appengine/xmpp) = %{version}

Requires:       go(github.com/golang/protobuf)
Requires:       go(golang.org/x/net/context)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/protobuf)

%description
This package provides the Go library google.golang.org/appengine.

%files
%doc README.md
%doc CONTRIBUTING.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
