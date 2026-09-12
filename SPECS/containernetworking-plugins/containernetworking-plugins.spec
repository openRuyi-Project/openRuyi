# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           plugins
%define go_import_path  github.com/containernetworking/plugins

# containerd's upstream Linux default and openRuyi's Calico manifest both use
# this CNI-specific compatibility path rather than the generic libexec path.
%global cni_bindir      /opt/cni/bin

Name:           containernetworking-plugins
Version:        1.9.1
Release:        %autorelease
Summary:        Standard networking plugins for the Container Network Interface
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND MIT AND MPL-2.0
URL:            https://github.com/containernetworking/plugins
VCS:            git:https://github.com/containernetworking/plugins.git
#!RemoteAsset:  sha256:34bd82d47e981940751619c9cc44c095bb90bfcaf8d71865cbb822c37690a764
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildSystem:    golang

BuildOption(prep):  -n %{_name}-%{version}

BuildRequires:  go >= 1.24.2
BuildRequires:  go-rpm-macros
BuildRequires:  systemd-rpm-macros

Requires:       iproute2
Requires:       iptables-nft
Requires:       nftables
%{?systemd_requires}
Provides:       cni-plugins = %{version}

%description
This package provides the reference CNI plugins used by container runtimes to
configure network interfaces, IP address management, and port mappings for
Linux containers.

%package     -n go-github-containernetworking-plugins
Summary:        Go libraries for Container Network Interface plugins
BuildArch:      noarch
Provides:       go(github.com/containernetworking/plugins) = %{version}
Provides:       go(github.com/containernetworking/plugins/pkg/ns) = %{version}

Requires:       go(golang.org/x/sys)

%description -n go-github-containernetworking-plugins
This package provides the reusable Go libraries for Container Network
Interface plugins, including the network namespace helper package.

%build
export CGO_ENABLED=1
export GOCACHE=%{_builddir}/go-build-cache
export GOFLAGS="-buildmode=pie -trimpath -modcacherw"
export GOTOOLCHAIN=local
./build_linux.sh %{go_build_flags_default} -ldflags "-s -w"

%install
install -dm0755 %{buildroot}%{cni_bindir}
install -pm0755 bin/* %{buildroot}%{cni_bindir}/
install -Dpm0644 plugins/ipam/dhcp/systemd/cni-dhcp.service \
    %{buildroot}%{_unitdir}/cni-dhcp.service
install -Dpm0644 plugins/ipam/dhcp/systemd/cni-dhcp.socket \
    %{buildroot}%{_unitdir}/cni-dhcp.socket

%buildsystem_golangmodules_install
go_source_root=%{buildroot}%{go_sys_gopath}/%{go_import_path}
rm -rf "${go_source_root}/bin" \
    "${go_source_root}/vendor" \
    "${go_source_root}/.github"
rm -f "${go_source_root}/.gitignore" \
    "${go_source_root}/.golangci.yml" \
    "${go_source_root}/.yamllint.yml" \
    "${go_source_root}/LICENSE" \
    "${go_source_root}/README.md" \
    "${go_source_root}/build_linux.sh" \
    "${go_source_root}/build_windows.sh" \
    "${go_source_root}/test_linux.sh" \
    "${go_source_root}/test_windows.sh" \
    "${go_source_root}/plugins/main/windows/build.sh"

%check
export CGO_ENABLED=1
export GOCACHE=%{_builddir}/go-test-cache
export GOFLAGS="-buildmode=pie -trimpath -mod=vendor -modcacherw"
export GOTOOLCHAIN=local

# Compile the complete Linux test suite without running privileged network tests.
go test -vet=off -run '^$' ./...

# CNI VERSION is an unprivileged execution check supported by every plugin.
plugin_count=0
for plugin in bin/*; do
    output=$(printf '{"cniVersion":"1.0.0"}' \
        | env CNI_COMMAND=VERSION "${plugin}")
    printf '%s\n' "${output}" | grep -q '"supportedVersions"'
    plugin_count=$((plugin_count + 1))
done
test "${plugin_count}" -eq 18

%post
%systemd_post cni-dhcp.socket

%preun
%systemd_preun cni-dhcp.socket cni-dhcp.service

%postun
%systemd_postun_with_restart cni-dhcp.socket cni-dhcp.service

%files
%doc README.md
%license LICENSE vendor/modules.txt
%dir /opt/cni
%dir %{cni_bindir}
%{cni_bindir}/*
%{_unitdir}/cni-dhcp.service
%{_unitdir}/cni-dhcp.socket

%files -n go-github-containernetworking-plugins
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
