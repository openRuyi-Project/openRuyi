# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           cloudpods-operator
Version:        4.0.3
Release:        %autorelease
Summary:        Kubernetes operator for Cloudpods
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0
URL:            https://github.com/yunionio/cloudpods-operator
VCS:            git:https://github.com/yunionio/cloudpods-operator.git
#!RemoteAsset:  sha256:3b0549875cce552c815ff16f740b14cc8ec658ef56eb5625e6aefeccff241452
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/cloudpods-operator-%{version}.tar.gz
# Backport of upstream PR #1564. Preserve the original upstream authorship and
# drop this patch after the fix is merged and released.
Patch2000:      2000-respect-configured-etcd-busybox-image.patch

BuildRequires:  binutils
BuildRequires:  go >= 1.24
BuildRequires:  go-rpm-macros

Provides:       onecloud-operator = %{version}-%{release}

%description
Cloudpods Operator manages the lifecycle and configuration of Cloudpods
components on Kubernetes. This package also contains the compose service and
Telegraf initialization helpers used by the operator-managed workloads.

%prep
%autosetup -p1

%build
export CGO_ENABLED=1
export GOCACHE=%{_builddir}/go-build-cache
export GOFLAGS="-buildmode=pie -trimpath -mod=vendor -modcacherw"
export GOPROXY=off
export GOTOOLCHAIN=local

go_ldflags="-s -w -X yunion.io/x/onecloud-operator/pkg/version.Version=v%{version}"

install -dm0755 _output/bin
go build %{go_build_flags_default} -buildvcs=false \
    -ldflags "${go_ldflags}" \
    -o _output/bin/onecloud-controller-manager ./cmd/onecloud-operator
go build %{go_build_flags_default} -buildvcs=false \
    -ldflags "${go_ldflags}" \
    -o _output/bin/compose-service-init ./cmd/compose-service-init
go build %{go_build_flags_default} -buildvcs=false \
    -ldflags "${go_ldflags}" \
    -o _output/bin/telegraf-init ./cmd/telegraf-init

%install
install -Dpm0755 _output/bin/onecloud-controller-manager \
    %{buildroot}%{_bindir}/onecloud-controller-manager
install -Dpm0755 _output/bin/compose-service-init \
    %{buildroot}%{_libexecdir}/cloudpods-operator/compose-service-init
install -Dpm0755 _output/bin/telegraf-init \
    %{buildroot}%{_libexecdir}/cloudpods-operator/telegraf-init

%check
export CGO_ENABLED=1
export GOCACHE=%{_builddir}/go-test-cache
export GOFLAGS="-buildmode=pie -trimpath -mod=vendor -modcacherw"
export GOPROXY=off
export GOTOOLCHAIN=local

go test -vet=off ./pkg/manager/component -run 'Test_getRepoImageName'
test "$(%{buildroot}%{_bindir}/onecloud-controller-manager --version)" = "v%{version}"
test "$(%{buildroot}%{_libexecdir}/cloudpods-operator/compose-service-init --version)" = "v%{version}"
go version -m %{buildroot}%{_libexecdir}/cloudpods-operator/telegraf-init \
    | grep -q 'yunion.io/x/onecloud-operator'

%files
%doc README.md docs/intro.md manifests/*.yaml
%license LICENSE
%{_bindir}/onecloud-controller-manager
%dir %{_libexecdir}/cloudpods-operator
%{_libexecdir}/cloudpods-operator/compose-service-init
%{_libexecdir}/cloudpods-operator/telegraf-init

%changelog
%autochangelog
