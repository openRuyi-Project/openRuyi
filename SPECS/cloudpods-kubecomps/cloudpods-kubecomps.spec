# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit             eb381ed38b587e2cabd081c69a0e6b0aa04a5360
%global build_date         2026-05-12T10:36:59Z
%global source_date_epoch  1778582219
%global yunion_root        /opt/yunion

Name:           cloudpods-kubecomps
Version:        4.0.3
Release:        %autorelease
Summary:        Kubernetes management components for Cloudpods
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT AND MPL-2.0
URL:            https://github.com/yunionio/kubecomps
VCS:            git:https://github.com/yunionio/kubecomps.git
#!RemoteAsset:  sha256:0598423e451151e621410867f643f56286b35ef9e1760bb5a5190c5d458cc98f
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/kubecomps-%{version}.tar.gz
# The upstream release uses three gitlinks to a Kubespray fork. This archive
# preserves the exact pinned commits for offline builds and runtime use.
# TODO: Drop this archive when upstream release tarballs include the gitlink
# contents or provide an equivalent complete source archive.
#!RemoteAsset:  sha256:061b22383ce8c46a13c0b368ff2387dd2ef317392031d551d91718d8d093de5b
Source1:        https://github.com/software-vendor/kubecomps-ansible-vendor/releases/download/v%{version}/kubecomps-%{version}-ansible-vendor.tar.gz
# Helper used at build time to package upstream Helm chart directories with
# the same Helm library version already present in the upstream Go vendor tree.
Source2:        kubecomps-package-chart.go

BuildRequires:  binutils
BuildRequires:  ceph-devel
BuildRequires:  go >= 1.24
BuildRequires:  go-rpm-macros
BuildRequires:  gzip
BuildRequires:  tar

Requires:       cloudpods-kubeserver%{?_isa} = %{version}-%{release}

%description
Kubecomps contains the Kubernetes management components used by Cloudpods.
The main package is a convenience package that installs the KubeServer API
service, including its offline Helm and Ansible runtime assets.

%package        -n cloudpods-kubeserver
Summary:        Kubernetes management API service for Cloudpods
Provides:       yunion-kubeserver = %{version}-%{release}
Requires:       openssh-clients
# openRuyi's QEMU package also advertises the RDMA sonames from a private
# library directory, so librados dependencies alone may not pull in the
# loader-visible providers under the system library directory.
Requires:       rdma-core
Recommends:     ansible-core

%description    -n cloudpods-kubeserver
KubeServer manages Kubernetes clusters through Cloudpods. The package contains
the server executable, embedded Helm charts, and the exact Kubespray assets
pinned by the upstream v4.0.3 release.

%prep
%autosetup -n kubecomps-%{version}
tar -xzf %{SOURCE1} -C .
test -f manifests/ansible/kubespray/ansible_version.yml
test -f manifests/ansible/kubespray_2_17_0/ansible_version.yml
test -f manifests/ansible/kubespray_2_19_1/ansible_version.yml

%build
export CGO_ENABLED=1
export GOCACHE=%{_builddir}/go-build-cache
export GOFLAGS="-buildmode=pie -trimpath -mod=vendor -modcacherw"
export GOPROXY=off
export GOTOOLCHAIN=local
export SOURCE_DATE_EPOCH=%{source_date_epoch}

install -dm0755 static _chart-unpack _output/bin
charts="monitor-stack monitor-stack-v2 minio thanos fluent-bit \
aws-load-balancer-controller aws-ebs-csi-driver"
for chart in ${charts}; do
    go run -mod=vendor %{SOURCE2} "manifests/helm/${chart}" static
done

# Helm 3.4 writes the current time into chart archives. Normalize every
# generated archive before embedding it so repeated RPM builds are identical.
for archive in static/*.tgz; do
    archive_name="$(basename "${archive}")"
    unpack_dir="_chart-unpack/${archive_name%.tgz}"
    install -dm0755 "${unpack_dir}"
    tar -xzf "${archive}" -C "${unpack_dir}"
    chart_root="$(tar -tzf "${archive}" | head -n 1 | cut -d/ -f1)"
    test -n "${chart_root}"
    tar --format=gnu --sort=name --owner=0 --group=0 --numeric-owner \
        --mtime="@%{source_date_epoch}" -cf - \
        -C "${unpack_dir}" "${chart_root}" \
        | gzip -n > "${archive}.normalized"
    mv "${archive}.normalized" "${archive}"
done

cp -a manifests/grafana-dashboards/. static/
go generate -mod=vendor ./pkg/kubeserver/embed
test -s pkg/kubeserver/embed/zz_generated.blob.go

go_ldflags="-s -w \
    -X yunion.io/x/pkg/util/version.gitVersion=v%{version} \
    -X yunion.io/x/pkg/util/version.gitCommit=%{commit} \
    -X yunion.io/x/pkg/util/version.gitBranch=release/4.0 \
    -X yunion.io/x/pkg/util/version.gitTreeState=clean \
    -X yunion.io/x/pkg/util/version.buildDate=%{build_date}"

go build %{go_build_flags_default} -buildvcs=false \
    -ldflags "${go_ldflags}" \
    -o _output/bin/kubeserver ./cmd/kubeserver

%install
install -Dpm0755 _output/bin/kubeserver \
    %{buildroot}%{_bindir}/kubeserver
install -dm0755 %{buildroot}%{_datadir}/cloudpods-kubecomps/ansible
cp -a manifests/ansible/. \
    %{buildroot}%{_datadir}/cloudpods-kubecomps/ansible/

# Keep the paths used by the upstream KubeServer container while storing the
# real binary and architecture-independent data under standard RPM paths.
install -dm0755 %{buildroot}%{yunion_root}/bin
ln -s ../../../usr/bin/kubeserver \
    %{buildroot}%{yunion_root}/bin/kubeserver
ln -s kubeserver %{buildroot}%{yunion_root}/bin/kube-server
ln -s ../../usr/share/cloudpods-kubecomps/ansible \
    %{buildroot}%{yunion_root}/ansible

%check
export CGO_ENABLED=1
export GOCACHE=%{_builddir}/go-test-cache
export GOFLAGS="-buildmode=pie -trimpath -mod=vendor -modcacherw"
export GOPROXY=off
export GOTOOLCHAIN=local

go test -vet=off ./pkg/kubeserver/embed \
    ./pkg/kubeserver/drivers/clusters/kubespray
%{buildroot}%{_bindir}/kubeserver --help 2>&1 | grep -q 'https-port'
strings %{buildroot}%{_bindir}/kubeserver \
    | grep -q 'monitor-stack-v2-55.11.0.tgz'
test -x %{buildroot}%{_datadir}/cloudpods-kubecomps/ansible/kubespray/contrib/aws_inventory/kubespray-aws-inventory.py

%files
%doc README.md README-CN.md
%license LICENSE

%files -n cloudpods-kubeserver
%doc vendor/modules.txt
%license LICENSE
%{_bindir}/kubeserver
%dir %{_datadir}/cloudpods-kubecomps
%{_datadir}/cloudpods-kubecomps/ansible
%dir %{yunion_root}
%dir %{yunion_root}/bin
%{yunion_root}/bin/kubeserver
%{yunion_root}/bin/kube-server
%{yunion_root}/ansible

%changelog
%autochangelog
