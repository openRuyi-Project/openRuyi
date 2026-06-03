# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name hf-hub
%global full_version 0.4.1
%global pkgname hf-hub-0.4

Name:           rust-hf-hub-0.4
Version:        0.4.1
Release:        %autorelease
Summary:        Rust crate "hf-hub"
License:        Apache-2.0
URL:            https://github.com/huggingface/hf-hub
#!RemoteAsset:  sha256:112fa2f6ad4ab815b9e1b938b4b1e437032d055e2f92ed10fd6ab2e62d02c6b6
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(dirs-5.0/default) >= 5.0.1
Requires:       crate(log-0.4/default) >= 0.4.29
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "hf-hub"

%package     -n %{name}+default
Summary:        This crates aims ease the interaction with [huggingface](https://huggingface.co/)  It aims to be compatible with [huggingface_hub](https://github.com/huggingface/huggingface_hub/) python package, but only implements a smaller subset of functions - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/default-tls)
Requires:       crate(%{pkgname}/tokio)
Requires:       crate(%{pkgname}/ureq)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust hf-hub crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+native-tls
Summary:        This crates aims ease the interaction with [huggingface](https://huggingface.co/)  It aims to be compatible with [huggingface_hub](https://github.com/huggingface/huggingface_hub/) python package, but only implements a smaller subset of functions - feature "native-tls" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(native-tls-0.2/default) >= 0.2.12
Requires:       crate(reqwest-0.12/default) >= 0.12.28
Requires:       crate(reqwest-0.12/json) >= 0.12.28
Requires:       crate(reqwest-0.12/stream) >= 0.12.28
Requires:       crate(ureq-2.0/json) >= 2.12.1
Requires:       crate(ureq-2.0/native-tls) >= 2.12.1
Requires:       crate(ureq-2.0/socks-proxy) >= 2.12.1
Provides:       crate(%{pkgname}/default-tls)
Provides:       crate(%{pkgname}/native-tls)

%description -n %{name}+native-tls
This metapackage enables feature "native-tls" for the Rust hf-hub crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default-tls" feature.

%package     -n %{name}+rustls-tls
Summary:        This crates aims ease the interaction with [huggingface](https://huggingface.co/)  It aims to be compatible with [huggingface_hub](https://github.com/huggingface/huggingface_hub/) python package, but only implements a smaller subset of functions - feature "rustls-tls"
Requires:       crate(%{pkgname})
Requires:       crate(reqwest-0.12/json) >= 0.12.28
Requires:       crate(reqwest-0.12/rustls-tls) >= 0.12.28
Requires:       crate(reqwest-0.12/stream) >= 0.12.28
Requires:       crate(rustls-0.23/default) >= 0.23.36
Provides:       crate(%{pkgname}/rustls-tls)

%description -n %{name}+rustls-tls
This metapackage enables feature "rustls-tls" for the Rust hf-hub crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        This crates aims ease the interaction with [huggingface](https://huggingface.co/)  It aims to be compatible with [huggingface_hub](https://github.com/huggingface/huggingface_hub/) python package, but only implements a smaller subset of functions - feature "tokio"
Requires:       crate(%{pkgname})
Requires:       crate(futures-0.3/default) >= 0.3.28
Requires:       crate(indicatif-0.17/default) >= 0.17.11
Requires:       crate(num-cpus-1.0/default) >= 1.15.0
Requires:       crate(rand-0.8/default) >= 0.8.5
Requires:       crate(reqwest-0.12/charset) >= 0.12.28
Requires:       crate(reqwest-0.12/http2) >= 0.12.28
Requires:       crate(reqwest-0.12/json) >= 0.12.28
Requires:       crate(reqwest-0.12/macos-system-configuration) >= 0.12.28
Requires:       crate(reqwest-0.12/stream) >= 0.12.28
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-1.0/derive) >= 1.0.228
Requires:       crate(serde-json-1.0/default) >= 1.0.149
Requires:       crate(thiserror-2.0/default) >= 2.0.17
Requires:       crate(tokio-1.0/default) >= 1.29.1
Requires:       crate(tokio-1.0/fs) >= 1.29.1
Requires:       crate(tokio-1.0/macros) >= 1.29.1
Requires:       crate(tokio-1.0/rt-multi-thread) >= 1.29.1
Provides:       crate(%{pkgname}/tokio)

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust hf-hub crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ureq
Summary:        This crates aims ease the interaction with [huggingface](https://huggingface.co/)  It aims to be compatible with [huggingface_hub](https://github.com/huggingface/huggingface_hub/) python package, but only implements a smaller subset of functions - feature "ureq"
Requires:       crate(%{pkgname})
Requires:       crate(http-1.0/default) >= 1.4.0
Requires:       crate(indicatif-0.17/default) >= 0.17.11
Requires:       crate(rand-0.8/default) >= 0.8.5
Requires:       crate(serde-1.0/default) >= 1.0.228
Requires:       crate(serde-1.0/derive) >= 1.0.228
Requires:       crate(serde-json-1.0/default) >= 1.0.149
Requires:       crate(thiserror-2.0/default) >= 2.0.17
Requires:       crate(ureq-2.0/default) >= 2.12.1
Requires:       crate(ureq-2.0/json) >= 2.12.1
Requires:       crate(ureq-2.0/socks-proxy) >= 2.12.1
Provides:       crate(%{pkgname}/ureq)

%description -n %{name}+ureq
This metapackage enables feature "ureq" for the Rust hf-hub crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
