# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: wangyf0611 <wangyufeng@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# UTC timestamp of the commit referenced by the upstream v4.0.3 tag.
%global source_date_epoch  1779362913
%global yarn_version       1.22.22

Name:           cloudpods-dashboard
Version:        4.0.3
Release:        %autorelease
Summary:        Web dashboard for Cloudpods
License:        AGPL-3.0-only AND 0BSD AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BlueOak-1.0.0 AND CC-BY-3.0 AND CC-BY-4.0 AND CC0-1.0 AND ISC AND MIT AND MPL-2.0 AND Unlicense AND WTFPL AND Zlib
URL:            https://github.com/yunionio/dashboard
VCS:            git:https://github.com/yunionio/dashboard.git
#!RemoteAsset:  sha256:c26cd6533d6356fdd5ad913a41bdc4407f2344d820b96176da037aa107e9e473
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/dashboard-%{version}.tar.gz
# Original registry archives selected by the upstream yarn.lock.
#!RemoteAsset:  sha256:6ad741645408ac7ec87553e877f2361c3091458bab8ca88a59d8d1add9e90d0d
Source1:        https://github.com/software-vendor/cloudpods-dashboard-yarn-vendor/releases/download/v%{version}/cloudpods-dashboard-yarn-vendor-%{version}-r3.tar.gz
#!RemoteAsset:  sha256:88268464199d1611fcf73ce9c0a6c4d44c7d5363682720d8506f6508addf36a0
Source2:        https://github.com/yarnpkg/yarn/releases/download/v%{yarn_version}/yarn-v%{yarn_version}.tar.gz
# Backport the v4.0.3 RISC-V UI support. Drop after upstream PR #9920 is released.
Patch2000:      2000-feat-compute-add-riscv64-architecture-support.patch
# Tagged archives have no Git metadata. Keep normal checkout behavior unchanged.
Patch2001:      2001-build-allow-reproducible-metadata-without-Git.patch
# The offline dependency uses Math.random() in production builds. Apply this
# after Yarn installs node_modules to make SOURCE_DATE_EPOCH builds repeatable.
Patch2002:      2002-build-use-source-date-epoch-for-theme-config-key.patch
BuildArch:      noarch

BuildRequires:  nodejs >= 20

Provides:       onecloud-dashboard = %{version}-%{release}
Recommends:     nginx

%description
Cloudpods Dashboard is the web interface for managing Cloudpods resources.
This package contains architecture-independent production static assets.

%prep
%autosetup -n dashboard-%{version} -N
%patch -P 2000 -p1
%patch -P 2001 -p1
tar -xzf %{SOURCE1} -C %{_builddir}
tar -xzf %{SOURCE2} -C %{_builddir}

%build
node_options=--openssl-legacy-provider
export NODE_OPTIONS="${node_options}"
export SOURCE_DATE_EPOCH=%{source_date_epoch}
export DASHBOARD_SOURCE_COMMIT=v%{version}
export DASHBOARD_SOURCE_COMMITTER=GitHub
export DASHBOARD_SOURCE_REF=refs/tags/v%{version}
export YARN_YARN_OFFLINE_MIRROR=%{_builddir}/cloudpods-dashboard-yarn-vendor-%{version}/packages

yarn_js=%{_builddir}/yarn-v%{yarn_version}/bin/yarn.js
yarn_cache=%{_builddir}/yarn-cache

node "${yarn_js}" install \
    --offline \
    --frozen-lockfile \
    --ignore-engines \
    --ignore-scripts \
    --non-interactive \
    --cache-folder "${yarn_cache}"
patch --fuzz=0 -p1 < %{PATCH2002}
node "${yarn_js}" licenses generate-disclaimer --ignore-engines > THIRD_PARTY_NOTICES.txt
# Work around a Node.js 24/V8 optimizing-JIT crash observed during the native
# RISC-V build while retaining WebAssembly, which Webpack 4 uses for MD4.
# Use the same command on every architecture so the noarch payload is uniform.
node --no-opt --max_old_space_size=4096 \
    node_modules/@vue/cli-service/bin/vue-cli-service.js build

%install
install -dm0755 %{buildroot}%{_datadir}/cloudpods-dashboard
# Source maps are not needed at runtime and their module ordering varies with
# the build architecture even when the emitted JavaScript is identical.
find dist -type f -name '*.map' -delete
cp -a dist/. %{buildroot}%{_datadir}/cloudpods-dashboard/
find %{buildroot}%{_datadir}/cloudpods-dashboard -type f -exec chmod 0644 {} +

%check
export NODE_OPTIONS=--openssl-legacy-provider
yarn_js=%{_builddir}/yarn-v%{yarn_version}/bin/yarn.js
# Exercise the architecture mapping added by Patch2000.
node "${yarn_js}" test:unit --runInBand tests/unit/compute-arch.spec.js
# Verify that the production payload is complete, contains RISC-V support,
# omits non-runtime source maps, and ships generated dependency notices.
test -s %{buildroot}%{_datadir}/cloudpods-dashboard/index.html
test -n "$(find %{buildroot}%{_datadir}/cloudpods-dashboard/js -name 'app.*.js' -print -quit)"
grep -Rqs 'riscv64' %{buildroot}%{_datadir}/cloudpods-dashboard/js
test -z "$(find %{buildroot}%{_datadir}/cloudpods-dashboard -name '*.map' -print -quit)"
test -s THIRD_PARTY_NOTICES.txt

%files
%doc README.md README-CN.md conf/nginx.conf THIRD_PARTY_NOTICES.txt
%license LICENSE
%{_datadir}/cloudpods-dashboard

%changelog
%autochangelog
