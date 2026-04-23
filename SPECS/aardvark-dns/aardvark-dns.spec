# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: corestudy <2760018909@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           aardvark-dns
Version:        1.17.1
Release:        %autorelease
License:        Apache-2.0 AND MIT AND Zlib
Summary:        Authoritative DNS server for A/AAAA container records
URL:            https://github.com/containers/aardvark-dns
#!RemoteAsset:  sha256:25b39bfad079a03862825b2f9db8b71b82fc80aad5552a9c76ea912edc9b889e
Source0:        %{url}/archive/v%{version}.tar.gz
# TODO: use our own crates in the future
#!RemoteAsset:  sha256:009198f042f150d42025c8a0456bb7a98293c9deeb012d37b2d364f44e52288f
Source1:        %{url}/releases/download/v%{version}/%{name}-v%{version}-vendor.tar.gz
# TODO: use build system cargo in the future
BuildSystem:    autotools

BuildOption(build):  CARGO="cargo --offline"
BuildOption(install):  DESTDIR=%{buildroot}
BuildOption(install):  PREFIX=%{_prefix}

BuildRequires:  cargo
BuildRequires:  make
BuildRequires:  rust

%description
%{summary}

Forwards other request to configured resolvers.
Read more about configuration in `src/backend/mod.rs`.

%prep -a
tar xzf %{SOURCE1}
mkdir -p .cargo
cat << EOF > .cargo/config.toml
[target.'cfg(linux)']
runner = 'unshare -rn'

[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%conf
# there's no configure

%check
# there's no check

%files
%license LICENSE
%dir %{_libexecdir}/podman
%{_libexecdir}/podman/%{name}

%changelog
%autochangelog
