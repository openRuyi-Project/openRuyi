# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit          ba3601b84660226f57b2fdef60ed58ff1bf85b00
%global build_date      2026-05-27T03:50:35Z
%global go_import_path  yunion.io/x/onecloud
%global _name           cloudpods
%global yunion_bindir   /opt/yunion/bin

Name:           cloudpods
Version:        4.0.3
Release:        %autorelease
Summary:        Cloud-native multi-cloud and virtualization platform
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT
URL:            https://github.com/yunionio/cloudpods
VCS:            git:https://github.com/yunionio/cloudpods.git
#!RemoteAsset:  sha256:d91afbe5834c1965f72df43b5dab931b856c36c31bbc97653d576797601d703d
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        cloudpods-executor.service
BuildSystem:    golang

# Parse the executor command line so the service can use Cloudpods' standard
# /run/onecloud/exec.sock endpoint. Upstream currently declares but does not
# parse the socket-path flag.
Patch2000:      2000-executor-server-parse-command-line-flags.patch

BuildRequires:  gcc
BuildRequires:  go >= 1.24
BuildRequires:  go-rpm-macros
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  systemd-rpm-macros

Requires:       %{name}-cli%{?_isa} = %{version}-%{release}
Requires:       %{name}-executor%{?_isa} = %{version}-%{release}

%description
Cloudpods is a cloud-native platform for managing private clouds, public cloud
accounts, and on-premises virtualization through a consistent API. This
package installs the command-line client and privileged host executor needed
for initial openRuyi integration.

%package        cli
Summary:        Command-line client for Cloudpods
Provides:       yunion-climc = %{version}-%{release}

%description    cli
The Cloudpods command-line client provides administrative access to Cloudpods
APIs and resources.

%package        executor
Summary:        Privileged command executor for Cloudpods hosts
Provides:       yunion-executor = %{version}-%{release}
Requires:       systemd
%{?systemd_requires}

%description    executor
The Cloudpods executor exposes a local Unix-domain socket used by Cloudpods
host services to run privileged operating-system commands.

%prep
%autosetup -n %{name}-%{version} -p1

%build
export CGO_ENABLED=1
export GOCACHE=%{_builddir}/go-build-cache
export GOFLAGS="-buildmode=pie -trimpath -mod=vendor -modcacherw"
export GOPROXY=off
export GOTOOLCHAIN=local

go_ldflags="-s -w \
    -X yunion.io/x/pkg/util/version.gitVersion=v%{version} \
    -X yunion.io/x/pkg/util/version.gitCommit=%{commit} \
    -X yunion.io/x/pkg/util/version.gitBranch=release/%{version} \
    -X yunion.io/x/pkg/util/version.buildDate=%{build_date} \
    -X yunion.io/x/pkg/util/version.gitTreeState=clean \
    -X yunion.io/x/pkg/util/version.gitMajor=4 \
    -X yunion.io/x/pkg/util/version.gitMinor=0"

install -dm0755 _output/bin
go build %{go_build_flags_default} -ldflags "${go_ldflags}" \
    -o _output/bin/climc ./cmd/climc
go build %{go_build_flags_default} -ldflags "${go_ldflags}" \
    -o _output/bin/executor-server ./cmd/executor-server

%install
install -Dpm0755 _output/bin/climc %{buildroot}%{_bindir}/climc
install -Dpm0755 _output/bin/executor-server \
    %{buildroot}%{_libexecdir}/cloudpods/executor-server
install -Dpm0644 %{SOURCE1} \
    %{buildroot}%{_unitdir}/cloudpods-executor.service

install -dm0755 %{buildroot}%{bash_completions_dir}
%{buildroot}%{_bindir}/climc --completion bash \
    > %{buildroot}%{bash_completions_dir}/climc
install -dm0755 %{buildroot}%{zsh_completions_dir}
%{buildroot}%{_bindir}/climc --completion zsh \
    > %{buildroot}%{zsh_completions_dir}/_climc

# ocboot and existing Cloudpods automation use this upstream compatibility
# path, while the packaged executable itself remains in the standard bindir.
install -dm0755 %{buildroot}%{yunion_bindir}
ln -s ../../../usr/bin/climc %{buildroot}%{yunion_bindir}/climc

%check
export CGO_ENABLED=1
export GOCACHE=%{_builddir}/go-test-cache
export GOFLAGS="-buildmode=pie -trimpath -mod=vendor -modcacherw"
export GOPROXY=off
export GOTOOLCHAIN=local

go test -vet=off ./cmd/climc/... ./cmd/executor-server/...
%{buildroot}%{_bindir}/climc --help >/dev/null
%{buildroot}%{_bindir}/climc --completion bash | grep -q 'climc'
%{buildroot}%{_bindir}/climc --version \
    | grep -q '"gitCommit": "%{commit}"'
%{buildroot}%{_libexecdir}/cloudpods/executor-server --help 2>&1 \
    | grep -q -- '-socket-path'

%post executor
%systemd_post cloudpods-executor.service

%preun executor
%systemd_preun cloudpods-executor.service

%postun executor
%systemd_postun_with_restart cloudpods-executor.service

%files
%doc README.md README-CN.md
%license LICENSE

%files cli
%doc cmd/climc/README.md
%license LICENSE vendor/modules.txt
%{_bindir}/climc
%{bash_completions_dir}/climc
%{zsh_completions_dir}/_climc
%dir /opt/yunion
%dir %{yunion_bindir}
%{yunion_bindir}/climc

%files executor
%license LICENSE vendor/modules.txt
%dir %{_libexecdir}/cloudpods
%{_libexecdir}/cloudpods/executor-server
%{_unitdir}/cloudpods-executor.service

%changelog
%autochangelog
