# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           functions-framework-go
%define go_import_path  github.com/GoogleCloudPlatform/functions-framework-go

Name:           go-github-googlecloudplatform-functions-framework-go
Version:        1.9.2
Release:        %autorelease
Summary:        Functions Framework for portable Go functions
License:        Apache-2.0
URL:            https://github.com/GoogleCloudPlatform/functions-framework-go
#!RemoteAsset:  sha256:634aa525b5bdeaf4be163cdb3d735f7e8216fd8a3bf52a4e030561b5b8fa1193
Source0:        https://github.com/GoogleCloudPlatform/functions-framework-go/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(cloud.google.com/go/functions)
BuildRequires:  go(github.com/cloudevents/sdk-go/v2)
BuildRequires:  go(github.com/google/go-cmp)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/modern-go/concurrent)
BuildRequires:  go(github.com/modern-go/reflect2)
BuildRequires:  go(go.uber.org/atomic)
BuildRequires:  go(go.uber.org/multierr)
BuildRequires:  go(go.uber.org/zap)

Provides:       go(github.com/GoogleCloudPlatform/functions-framework-go) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/functions-framework-go/funcframework) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/functions-framework-go/functions) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/functions-framework-go/internal/events/pubsub) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/functions-framework-go/internal/fftypes) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/functions-framework-go/internal/registry) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/functions-framework-go/testdata/conformance/cmd/cloudevent) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/functions-framework-go/testdata/conformance/cmd/declarative) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/functions-framework-go/testdata/conformance/cmd/http) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/functions-framework-go/testdata/conformance/cmd/legacyevent) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/functions-framework-go/testdata/conformance/function) = %{version}
Provides:       go(github.com/GoogleCloudPlatform/functions-framework-go/testdata/conformance/nondeclarative) = %{version}

Requires:       go(cloud.google.com/go/functions)
Requires:       go(github.com/cloudevents/sdk-go/v2)

%description
This package provides the complete Functions Framework for Go repository,
including HTTP, background event, and CloudEvent handlers and test fixtures.

%install -a
# The archive contains a generated x86-64 executable alongside its Go source.
rm -f %{buildroot}%{go_sys_gopath}/%{go_import_path}/testdata/conformance/cmd/http/http

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
