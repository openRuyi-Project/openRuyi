# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           alertmanager
%define go_import_path  github.com/prometheus/alertmanager

Name:           alertmanager
Version:        0.33.1
Release:        %autorelease
Summary:        Alert routing and notification service for Prometheus
License:        Apache-2.0
URL:            https://github.com/prometheus/alertmanager
#!RemoteAsset:  sha256:dfe372ecee0704e59e166a6d72f11a689d6b8756366696a0af9fdf801059129b
Source0:        https://github.com/prometheus/alertmanager/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
#!RemoteAsset:  sha256:1f63344e196e47ba7bfe27276f44c1da77e39fb76493e42b2cf0a50ca8f04321
Source1:        https://github.com/prometheus/alertmanager/releases/download/v%{version}/alertmanager-web-ui-%{version}.tar.gz
BuildSystem:    golangmodules

# Align Alertmanager v0.33.1 with the semantic conventions used by packaged
# OpenTelemetry 1.44; upstream main contains the same import update.
# https://github.com/prometheus/alertmanager/commit/a57a6da433a8cf8a7c065e0f0a8dc7d8343d7fab
Patch0:         1000-tracing-align-semantic-conventions-with-OpenTelemetry-1.44.patch
# Alert store garbage collection can take longer than the original 20 ms
# deadline under high concurrency.
Patch1:         2000-allow-alert-store-gc-to-settle.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/alecthomas/kingpin/v2)
BuildRequires:  go(github.com/alecthomas/units)
BuildRequires:  go(github.com/aws/aws-sdk-go-v2)
BuildRequires:  go(github.com/aws/smithy-go)
BuildRequires:  go(github.com/cenkalti/backoff/v4)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/coder/quartz)
BuildRequires:  go(github.com/emersion/go-smtp)
BuildRequires:  go(github.com/fsnotify/fsnotify)
BuildRequires:  go(github.com/go-openapi/analysis)
BuildRequires:  go(github.com/go-openapi/errors)
BuildRequires:  go(github.com/go-openapi/loads)
BuildRequires:  go(github.com/go-openapi/runtime)
BuildRequires:  go(github.com/go-openapi/spec)
BuildRequires:  go(github.com/go-openapi/strfmt)
BuildRequires:  go(github.com/go-openapi/swag)
BuildRequires:  go(github.com/go-openapi/validate)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/hashicorp/go-sockaddr)
BuildRequires:  go(github.com/hashicorp/golang-lru)
BuildRequires:  go(github.com/hashicorp/memberlist)
BuildRequires:  go(github.com/jessevdk/go-flags)
BuildRequires:  go(github.com/KimMachineGun/automemlimit)
BuildRequires:  go(github.com/oklog/run)
BuildRequires:  go(github.com/oklog/ulid/v2)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(github.com/prometheus/exporter-toolkit)
BuildRequires:  go(github.com/prometheus/sigv4)
BuildRequires:  go(github.com/rs/cors)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(github.com/twmb/franz-go)
BuildRequires:  go(github.com/xlab/treeprint)
BuildRequires:  go(go.opentelemetry.io/auto/sdk)
BuildRequires:  go(go.opentelemetry.io/contrib)
BuildRequires:  go(go.opentelemetry.io/otel)
BuildRequires:  go(go.opentelemetry.io/proto)
BuildRequires:  go(golang.org/x/mod)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/text)
BuildRequires:  go(google.golang.org/grpc)
BuildRequires:  go(google.golang.org/protobuf)
BuildRequires:  go(gopkg.in/telebot.v3)
BuildRequires:  go(gopkg.in/yaml.v2)
BuildRequires:  tzdata

Requires:       tzdata

%package     -n go-github-prometheus-alertmanager
Summary:        Go source for Prometheus Alertmanager
BuildArch:      noarch
Provides:       go(github.com/prometheus/alertmanager) = %{version}

Requires:       go(github.com/alecthomas/kingpin/v2)
Requires:       go(github.com/alecthomas/units)
Requires:       go(github.com/aws/aws-sdk-go-v2)
Requires:       go(github.com/aws/smithy-go)
Requires:       go(github.com/cenkalti/backoff/v4)
Requires:       go(github.com/cespare/xxhash/v2)
Requires:       go(github.com/coder/quartz)
Requires:       go(github.com/fsnotify/fsnotify)
Requires:       go(github.com/go-openapi/analysis)
Requires:       go(github.com/go-openapi/errors)
Requires:       go(github.com/go-openapi/loads)
Requires:       go(github.com/go-openapi/runtime)
Requires:       go(github.com/go-openapi/spec)
Requires:       go(github.com/go-openapi/strfmt)
Requires:       go(github.com/go-openapi/swag)
Requires:       go(github.com/go-openapi/validate)
Requires:       go(github.com/google/uuid)
Requires:       go(github.com/hashicorp/go-sockaddr)
Requires:       go(github.com/hashicorp/golang-lru)
Requires:       go(github.com/hashicorp/memberlist)
Requires:       go(github.com/jessevdk/go-flags)
Requires:       go(github.com/KimMachineGun/automemlimit)
Requires:       go(github.com/oklog/run)
Requires:       go(github.com/oklog/ulid/v2)
Requires:       go(github.com/prometheus/client_golang)
Requires:       go(github.com/prometheus/client_model)
Requires:       go(github.com/prometheus/common)
Requires:       go(github.com/prometheus/exporter-toolkit)
Requires:       go(github.com/prometheus/sigv4)
Requires:       go(github.com/rs/cors)
Requires:       go(github.com/twmb/franz-go)
Requires:       go(github.com/xlab/treeprint)
Requires:       go(go.opentelemetry.io/auto/sdk)
Requires:       go(go.opentelemetry.io/contrib)
Requires:       go(go.opentelemetry.io/otel)
Requires:       go(go.opentelemetry.io/proto)
Requires:       go(golang.org/x/mod)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/text)
Requires:       go(google.golang.org/grpc)
Requires:       go(google.golang.org/protobuf)
Requires:       go(gopkg.in/telebot.v3)
Requires:       go(gopkg.in/yaml.v2)

%description
Alertmanager deduplicates, groups, and routes alerts from Prometheus and other
clients to configured notification integrations. It also manages silences and
alert inhibition.

%description -n go-github-prometheus-alertmanager
This package contains the Go source for Prometheus Alertmanager, including the
API models consumed by Prometheus and other Go applications.

%prep
%autosetup -n %{_name}-%{version} -p1
tar -xzf %{SOURCE1} -C ui/app

%build
%go_common
_version_ldflags="%{shrink:
    -X github.com/prometheus/common/version.Version=%{version}
    -X github.com/prometheus/common/version.Revision=packaged
    -X github.com/prometheus/common/version.Branch=release
    -X github.com/prometheus/common/version.BuildUser=openruyi
    -X github.com/prometheus/common/version.BuildDate=19700101-00:00:00
}"
%__go build %{go_build_flags_default} -ldflags "$_version_ldflags" -o %{_builddir}/alertmanager ./cmd/alertmanager
%__go build %{go_build_flags_default} -ldflags "$_version_ldflags" -o %{_builddir}/amtool ./cmd/amtool

%install
install -D -m 0755 %{_builddir}/alertmanager %{buildroot}%{_bindir}/alertmanager
install -D -m 0755 %{_builddir}/amtool %{buildroot}%{_bindir}/amtool
%buildsystem_golangmodules_install

%check
_go_pkgs=""
while IFS='|' read -r _kind _pkg _error; do
    if [ "$_kind" = error ]; then
        case "$_pkg" in
            %{go_import_path}/internal/tools*) continue ;;
        esac
        echo "go list failed for $_pkg: $_error" >&2
        exit 1
    fi
    case "$_pkg" in
        %{go_import_path}/internal/tools*) continue ;;
    esac
    _go_pkgs="$_go_pkgs $_pkg"
done < <(go list -e -f '{{if .Error}}error|{{.ImportPath}}|{{.Error.Err}}{{else}}package|{{.ImportPath}}|{{end}}' ./...)
KGO_TEST_RF=1 go test -v $_go_pkgs

%files
%doc NOTICE README.md
%license LICENSE
%{_bindir}/alertmanager
%{_bindir}/amtool

%files -n go-github-prometheus-alertmanager
%doc NOTICE README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
