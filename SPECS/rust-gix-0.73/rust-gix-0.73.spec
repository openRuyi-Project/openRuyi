# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name gix
%global full_version 0.73.0
%global pkgname gix-0.73

Name:           rust-gix-0.73
Version:        0.73.0
Release:        %autorelease
Summary:        Rust crate "gix"
License:        MIT OR Apache-2.0
URL:            https://github.com/GitoxideLabs/gitoxide
#!RemoteAsset:  sha256:514c29cc879bdc0286b0cbc205585a49b252809eb86c69df4ce4f855ee75f635
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(gix-actor-0.35/default) >= 0.35.2
Requires:       crate(gix-commitgraph-0.29/default) >= 0.29.0
Requires:       crate(gix-config-0.46/default) >= 0.46.0
Requires:       crate(gix-date-0.10/default) >= 0.10.3
Requires:       crate(gix-diff-0.53) >= 0.53.0
Requires:       crate(gix-discover-0.41/default) >= 0.41.0
Requires:       crate(gix-features-0.43/default) >= 0.43.0
Requires:       crate(gix-features-0.43/once-cell) >= 0.43.0
Requires:       crate(gix-features-0.43/progress) >= 0.43.0
Requires:       crate(gix-fs-0.16/default) >= 0.16.0
Requires:       crate(gix-glob-0.21/default) >= 0.21.0
Requires:       crate(gix-hash-0.19/default) >= 0.19.0
Requires:       crate(gix-hashtable-0.9/default) >= 0.9.0
Requires:       crate(gix-lock-18/default) >= 18.0.0
Requires:       crate(gix-object-0.50/default) >= 0.50.0
Requires:       crate(gix-odb-0.70/default) >= 0.70.0
Requires:       crate(gix-pack-0.60/object-cache-dynamic) >= 0.60.0
Requires:       crate(gix-path-0.10/default) >= 0.10.19
Requires:       crate(gix-protocol-0.51/default) >= 0.51.0
Requires:       crate(gix-ref-0.53/default) >= 0.53.0
Requires:       crate(gix-refspec-0.31/default) >= 0.31.0
Requires:       crate(gix-revision-0.35) >= 0.35.0
Requires:       crate(gix-revwalk-0.21/default) >= 0.21.0
Requires:       crate(gix-sec-0.12/default) >= 0.12.0
Requires:       crate(gix-shallow-0.5/default) >= 0.5.0
Requires:       crate(gix-tempfile-18) >= 18.0.0
Requires:       crate(gix-trace-0.1/default) >= 0.1.13
Requires:       crate(gix-traverse-0.47/default) >= 0.47.0
Requires:       crate(gix-url-0.32/default) >= 0.32.0
Requires:       crate(gix-utils-0.3/default) >= 0.3.0
Requires:       crate(gix-validate-0.10/default) >= 0.10.0
Requires:       crate(once-cell-1/default) >= 1.21.3
Requires:       crate(smallvec-1/default) >= 1.15.1
Requires:       crate(thiserror-2/default) >= 2.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/tree-editor) = %{version}

%description
Source code for takopackized Rust crate "gix"

%package     -n %{name}+async-network-client
Summary:        Interact with git repositories just like git would - feature "async-network-client"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/attributes) = %{version}
Requires:       crate(%{pkgname}/credentials) = %{version}
Requires:       crate(gix-pack-0.60/object-cache-dynamic) >= 0.60.0
Requires:       crate(gix-pack-0.60/streaming-input) >= 0.60.0
Requires:       crate(gix-protocol-0.51/async-client) >= 0.51.0
Requires:       crate(gix-transport-0.48/default) >= 0.48.0
Provides:       crate(%{pkgname}/async-network-client) = %{version}

%description -n %{name}+async-network-client
This metapackage enables feature "async-network-client" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-network-client-async-std
Summary:        Interact with git repositories just like git would - feature "async-network-client-async-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-network-client) = %{version}
Requires:       crate(%{pkgname}/async-std) = %{version}
Requires:       crate(gix-transport-0.48/async-std) >= 0.48.0
Provides:       crate(%{pkgname}/async-network-client-async-std) = %{version}

%description -n %{name}+async-network-client-async-std
This metapackage enables feature "async-network-client-async-std" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-std
Summary:        Interact with git repositories just like git would - feature "async-std"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-std-1/default) >= 1.12.0
Provides:       crate(%{pkgname}/async-std) = %{version}

%description -n %{name}+async-std
This metapackage enables feature "async-std" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+attributes
Summary:        Interact with git repositories just like git would - feature "attributes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/command) = %{version}
Requires:       crate(%{pkgname}/excludes) = %{version}
Requires:       crate(gix-attributes-0.27/default) >= 0.27.0
Requires:       crate(gix-filter-0.20/default) >= 0.20.0
Requires:       crate(gix-pathspec-0.12/default) >= 0.12.0
Requires:       crate(gix-submodule-0.20/default) >= 0.20.0
Requires:       crate(gix-worktree-0.42/attributes) >= 0.42.0
Provides:       crate(%{pkgname}/attributes) = %{version}

%description -n %{name}+attributes
This metapackage enables feature "attributes" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+basic
Summary:        Interact with git repositories just like git would - feature "basic"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/blob-diff) = %{version}
Requires:       crate(%{pkgname}/index) = %{version}
Requires:       crate(%{pkgname}/revision) = %{version}
Provides:       crate(%{pkgname}/basic) = %{version}

%description -n %{name}+basic
This metapackage enables feature "basic" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blame
Summary:        Interact with git repositories just like git would - feature "blame"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gix-blame-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/blame) = %{version}

%description -n %{name}+blame
This metapackage enables feature "blame" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blob-diff
Summary:        Interact with git repositories just like git would - feature "blob-diff"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/attributes) = %{version}
Requires:       crate(gix-diff-0.53/blob) >= 0.53.0
Provides:       crate(%{pkgname}/blob-diff) = %{version}

%description -n %{name}+blob-diff
This metapackage enables feature "blob-diff" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blocking-http-transport-curl
Summary:        Interact with git repositories just like git would - feature "blocking-http-transport-curl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/blocking-network-client) = %{version}
Requires:       crate(gix-transport-0.48/http-client-curl) >= 0.48.0
Provides:       crate(%{pkgname}/blocking-http-transport-curl) = %{version}

%description -n %{name}+blocking-http-transport-curl
This metapackage enables feature "blocking-http-transport-curl" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blocking-http-transport-curl-rustls
Summary:        Interact with git repositories just like git would - feature "blocking-http-transport-curl-rustls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/blocking-http-transport-curl) = %{version}
Requires:       crate(gix-transport-0.48/http-client-curl-rust-tls) >= 0.48.0
Provides:       crate(%{pkgname}/blocking-http-transport-curl-rustls) = %{version}

%description -n %{name}+blocking-http-transport-curl-rustls
This metapackage enables feature "blocking-http-transport-curl-rustls" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blocking-http-transport-reqwest
Summary:        Interact with git repositories just like git would - feature "blocking-http-transport-reqwest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/blocking-network-client) = %{version}
Requires:       crate(gix-transport-0.48/http-client-reqwest) >= 0.48.0
Provides:       crate(%{pkgname}/blocking-http-transport-reqwest) = %{version}

%description -n %{name}+blocking-http-transport-reqwest
This metapackage enables feature "blocking-http-transport-reqwest" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blocking-http-transport-reqwest-native-tls
Summary:        Interact with git repositories just like git would - feature "blocking-http-transport-reqwest-native-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/blocking-http-transport-reqwest) = %{version}
Requires:       crate(gix-transport-0.48/http-client-reqwest-native-tls) >= 0.48.0
Provides:       crate(%{pkgname}/blocking-http-transport-reqwest-native-tls) = %{version}

%description -n %{name}+blocking-http-transport-reqwest-native-tls
This metapackage enables feature "blocking-http-transport-reqwest-native-tls" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blocking-http-transport-reqwest-rust-tls
Summary:        Interact with git repositories just like git would - feature "blocking-http-transport-reqwest-rust-tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/blocking-http-transport-reqwest) = %{version}
Requires:       crate(gix-transport-0.48/http-client-reqwest-rust-tls) >= 0.48.0
Provides:       crate(%{pkgname}/blocking-http-transport-reqwest-rust-tls) = %{version}

%description -n %{name}+blocking-http-transport-reqwest-rust-tls
This metapackage enables feature "blocking-http-transport-reqwest-rust-tls" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blocking-http-transport-reqwest-rust-tls-trust-dns
Summary:        Interact with git repositories just like git would - feature "blocking-http-transport-reqwest-rust-tls-trust-dns"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/blocking-http-transport-reqwest) = %{version}
Requires:       crate(gix-transport-0.48/http-client-reqwest-rust-tls-trust-dns) >= 0.48.0
Provides:       crate(%{pkgname}/blocking-http-transport-reqwest-rust-tls-trust-dns) = %{version}

%description -n %{name}+blocking-http-transport-reqwest-rust-tls-trust-dns
This metapackage enables feature "blocking-http-transport-reqwest-rust-tls-trust-dns" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blocking-network-client
Summary:        Interact with git repositories just like git would - feature "blocking-network-client"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/attributes) = %{version}
Requires:       crate(%{pkgname}/credentials) = %{version}
Requires:       crate(gix-pack-0.60/object-cache-dynamic) >= 0.60.0
Requires:       crate(gix-pack-0.60/streaming-input) >= 0.60.0
Requires:       crate(gix-protocol-0.51/blocking-client) >= 0.51.0
Requires:       crate(gix-transport-0.48/default) >= 0.48.0
Provides:       crate(%{pkgname}/blocking-network-client) = %{version}

%description -n %{name}+blocking-network-client
This metapackage enables feature "blocking-network-client" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cache-efficiency-debug
Summary:        Interact with git repositories just like git would - feature "cache-efficiency-debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gix-features-0.43/cache-efficiency-debug) >= 0.43.0
Requires:       crate(gix-features-0.43/once-cell) >= 0.43.0
Requires:       crate(gix-features-0.43/progress) >= 0.43.0
Provides:       crate(%{pkgname}/cache-efficiency-debug) = %{version}

%description -n %{name}+cache-efficiency-debug
This metapackage enables feature "cache-efficiency-debug" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+comfort
Summary:        Interact with git repositories just like git would - feature "comfort"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gix-features-0.43/once-cell) >= 0.43.0
Requires:       crate(gix-features-0.43/progress) >= 0.43.0
Requires:       crate(gix-features-0.43/progress-unit-bytes) >= 0.43.0
Requires:       crate(gix-features-0.43/progress-unit-human-numbers) >= 0.43.0
Provides:       crate(%{pkgname}/comfort) = %{version}

%description -n %{name}+comfort
This metapackage enables feature "comfort" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+command
Summary:        Interact with git repositories just like git would - feature "command"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gix-command-0.6/default) >= 0.6.2
Provides:       crate(%{pkgname}/command) = %{version}

%description -n %{name}+command
This metapackage enables feature "command" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+credentials
Summary:        Interact with git repositories just like git would - feature "credentials"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gix-credentials-0.30/default) >= 0.30.0
Requires:       crate(gix-negotiate-0.21/default) >= 0.21.0
Requires:       crate(gix-prompt-0.11/default) >= 0.11.1
Provides:       crate(%{pkgname}/credentials) = %{version}

%description -n %{name}+credentials
This metapackage enables feature "credentials" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Interact with git repositories just like git would - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/basic) = %{version}
Requires:       crate(%{pkgname}/comfort) = %{version}
Requires:       crate(%{pkgname}/extras) = %{version}
Requires:       crate(%{pkgname}/max-performance-safe) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dirwalk
Summary:        Interact with git repositories just like git would - feature "dirwalk"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/attributes) = %{version}
Requires:       crate(%{pkgname}/excludes) = %{version}
Requires:       crate(gix-dir-0.15/default) >= 0.15.0
Provides:       crate(%{pkgname}/dirwalk) = %{version}

%description -n %{name}+dirwalk
This metapackage enables feature "dirwalk" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+document-features
Summary:        Interact with git repositories just like git would - feature "document-features"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features) = %{version}

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+excludes
Summary:        Interact with git repositories just like git would - feature "excludes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/index) = %{version}
Requires:       crate(gix-ignore-0.16/default) >= 0.16.0
Requires:       crate(gix-worktree-0.42) >= 0.42.0
Provides:       crate(%{pkgname}/excludes) = %{version}

%description -n %{name}+excludes
This metapackage enables feature "excludes" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+extras
Summary:        Interact with git repositories just like git would - feature "extras"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/attributes) = %{version}
Requires:       crate(%{pkgname}/credentials) = %{version}
Requires:       crate(%{pkgname}/dirwalk) = %{version}
Requires:       crate(%{pkgname}/excludes) = %{version}
Requires:       crate(%{pkgname}/interrupt) = %{version}
Requires:       crate(%{pkgname}/mailmap) = %{version}
Requires:       crate(%{pkgname}/revparse-regex) = %{version}
Requires:       crate(%{pkgname}/status) = %{version}
Requires:       crate(%{pkgname}/worktree-archive) = %{version}
Requires:       crate(%{pkgname}/worktree-mutation) = %{version}
Requires:       crate(%{pkgname}/worktree-stream) = %{version}
Provides:       crate(%{pkgname}/extras) = %{version}

%description -n %{name}+extras
This metapackage enables feature "extras" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gix-archive
Summary:        Interact with git repositories just like git would - feature "gix-archive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gix-archive-0.22) >= 0.22.0
Provides:       crate(%{pkgname}/gix-archive) = %{version}

%description -n %{name}+gix-archive
This metapackage enables feature "gix-archive" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gix-status
Summary:        Interact with git repositories just like git would - feature "gix-status"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gix-status-0.20/default) >= 0.20.0
Requires:       crate(gix-status-0.20/worktree-rewrites) >= 0.20.0
Provides:       crate(%{pkgname}/gix-status) = %{version}

%description -n %{name}+gix-status
This metapackage enables feature "gix-status" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gix-worktree-stream
Summary:        Interact with git repositories just like git would - feature "gix-worktree-stream"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gix-worktree-stream-0.22/default) >= 0.22.0
Provides:       crate(%{pkgname}/gix-worktree-stream) = %{version}

%description -n %{name}+gix-worktree-stream
This metapackage enables feature "gix-worktree-stream" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hp-tempfile-registry
Summary:        Interact with git repositories just like git would - feature "hp-tempfile-registry"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gix-tempfile-18/hp-hashmap) >= 18.0.0
Provides:       crate(%{pkgname}/hp-tempfile-registry) = %{version}

%description -n %{name}+hp-tempfile-registry
This metapackage enables feature "hp-tempfile-registry" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+index
Summary:        Interact with git repositories just like git would - feature "index"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gix-index-0.41/default) >= 0.41.0
Provides:       crate(%{pkgname}/index) = %{version}

%description -n %{name}+index
This metapackage enables feature "index" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+interrupt
Summary:        Interact with git repositories just like git would - feature "interrupt"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gix-tempfile-18/signals) >= 18.0.0
Requires:       crate(parking-lot-0.12/default) >= 0.12.4
Requires:       crate(signal-hook-0.3) >= 0.3.18
Provides:       crate(%{pkgname}/interrupt) = %{version}

%description -n %{name}+interrupt
This metapackage enables feature "interrupt" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mailmap
Summary:        Interact with git repositories just like git would - feature "mailmap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/revision) = %{version}
Requires:       crate(gix-mailmap-0.27/default) >= 0.27.2
Provides:       crate(%{pkgname}/mailmap) = %{version}

%description -n %{name}+mailmap
This metapackage enables feature "mailmap" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+max-control
Summary:        Interact with git repositories just like git would - feature "max-control" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/pack-cache-lru-dynamic) = %{version}
Requires:       crate(%{pkgname}/pack-cache-lru-static) = %{version}
Requires:       crate(%{pkgname}/parallel) = %{version}
Provides:       crate(%{pkgname}/max-control) = %{version}
Provides:       crate(%{pkgname}/max-performance) = %{version}
Provides:       crate(%{pkgname}/max-performance-safe) = %{version}

%description -n %{name}+max-control
This metapackage enables feature "max-control" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "max-performance", and "max-performance-safe" features.

%package     -n %{name}+merge
Summary:        Interact with git repositories just like git would - feature "merge"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/attributes) = %{version}
Requires:       crate(%{pkgname}/blob-diff) = %{version}
Requires:       crate(%{pkgname}/tree-editor) = %{version}
Requires:       crate(gix-merge-0.6) >= 0.6.0
Provides:       crate(%{pkgname}/merge) = %{version}

%description -n %{name}+merge
This metapackage enables feature "merge" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+need-more-recent-msrv
Summary:        Interact with git repositories just like git would - feature "need-more-recent-msrv"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/merge) = %{version}
Requires:       crate(%{pkgname}/tree-editor) = %{version}
Provides:       crate(%{pkgname}/need-more-recent-msrv) = %{version}

%description -n %{name}+need-more-recent-msrv
This metapackage enables feature "need-more-recent-msrv" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pack-cache-lru-dynamic
Summary:        Interact with git repositories just like git would - feature "pack-cache-lru-dynamic"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gix-pack-0.60/object-cache-dynamic) >= 0.60.0
Requires:       crate(gix-pack-0.60/pack-cache-lru-dynamic) >= 0.60.0
Provides:       crate(%{pkgname}/pack-cache-lru-dynamic) = %{version}

%description -n %{name}+pack-cache-lru-dynamic
This metapackage enables feature "pack-cache-lru-dynamic" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pack-cache-lru-static
Summary:        Interact with git repositories just like git would - feature "pack-cache-lru-static"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gix-pack-0.60/object-cache-dynamic) >= 0.60.0
Requires:       crate(gix-pack-0.60/pack-cache-lru-static) >= 0.60.0
Provides:       crate(%{pkgname}/pack-cache-lru-static) = %{version}

%description -n %{name}+pack-cache-lru-static
This metapackage enables feature "pack-cache-lru-static" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parallel
Summary:        Interact with git repositories just like git would - feature "parallel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gix-features-0.43/once-cell) >= 0.43.0
Requires:       crate(gix-features-0.43/parallel) >= 0.43.0
Requires:       crate(gix-features-0.43/progress) >= 0.43.0
Provides:       crate(%{pkgname}/parallel) = %{version}

%description -n %{name}+parallel
This metapackage enables feature "parallel" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+prodash
Summary:        Interact with git repositories just like git would - feature "prodash"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(prodash-30/default) >= 30.0.1
Requires:       crate(prodash-30/progress-tree) >= 30.0.1
Provides:       crate(%{pkgname}/prodash) = %{version}

%description -n %{name}+prodash
This metapackage enables feature "prodash" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+progress-tree
Summary:        Interact with git repositories just like git would - feature "progress-tree"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(prodash-30/progress-tree) >= 30.0.1
Provides:       crate(%{pkgname}/progress-tree) = %{version}

%description -n %{name}+progress-tree
This metapackage enables feature "progress-tree" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+regex
Summary:        Interact with git repositories just like git would - feature "regex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-1/std) >= 1.6.0
Provides:       crate(%{pkgname}/regex) = %{version}

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+revision
Summary:        Interact with git repositories just like git would - feature "revision"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/index) = %{version}
Requires:       crate(gix-revision-0.35/describe) >= 0.35.0
Requires:       crate(gix-revision-0.35/merge-base) >= 0.35.0
Provides:       crate(%{pkgname}/revision) = %{version}

%description -n %{name}+revision
This metapackage enables feature "revision" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+revparse-regex
Summary:        Interact with git repositories just like git would - feature "revparse-regex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/regex) = %{version}
Requires:       crate(%{pkgname}/revision) = %{version}
Provides:       crate(%{pkgname}/revparse-regex) = %{version}

%description -n %{name}+revparse-regex
This metapackage enables feature "revparse-regex" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Interact with git repositories just like git would - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gix-attributes-0.27/serde) >= 0.27.0
Requires:       crate(gix-commitgraph-0.29/serde) >= 0.29.0
Requires:       crate(gix-credentials-0.30/serde) >= 0.30.0
Requires:       crate(gix-ignore-0.16/serde) >= 0.16.0
Requires:       crate(gix-index-0.41/serde) >= 0.41.0
Requires:       crate(gix-mailmap-0.27/serde) >= 0.27.2
Requires:       crate(gix-object-0.50/serde) >= 0.50.0
Requires:       crate(gix-odb-0.70/serde) >= 0.70.0
Requires:       crate(gix-pack-0.60/object-cache-dynamic) >= 0.60.0
Requires:       crate(gix-pack-0.60/serde) >= 0.60.0
Requires:       crate(gix-protocol-0.51/serde) >= 0.51.0
Requires:       crate(gix-ref-0.53/serde) >= 0.53.0
Requires:       crate(gix-revision-0.35/serde) >= 0.35.0
Requires:       crate(gix-transport-0.48/serde) >= 0.48.0
Requires:       crate(gix-url-0.32/serde) >= 0.32.0
Requires:       crate(gix-worktree-0.42/serde) >= 0.42.0
Requires:       crate(serde-1/derive) >= 1.0.114
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+status
Summary:        Interact with git repositories just like git would - feature "status"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/blob-diff) = %{version}
Requires:       crate(%{pkgname}/dirwalk) = %{version}
Requires:       crate(%{pkgname}/gix-status) = %{version}
Requires:       crate(%{pkgname}/index) = %{version}
Requires:       crate(gix-diff-0.53/index) >= 0.53.0
Provides:       crate(%{pkgname}/status) = %{version}

%description -n %{name}+status
This metapackage enables feature "status" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Interact with git repositories just like git would - feature "tracing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gix-features-0.43/once-cell) >= 0.43.0
Requires:       crate(gix-features-0.43/progress) >= 0.43.0
Requires:       crate(gix-features-0.43/tracing) >= 0.43.0
Provides:       crate(%{pkgname}/tracing) = %{version}

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing-detail
Summary:        Interact with git repositories just like git would - feature "tracing-detail"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/tracing) = %{version}
Requires:       crate(gix-features-0.43/once-cell) >= 0.43.0
Requires:       crate(gix-features-0.43/progress) >= 0.43.0
Requires:       crate(gix-features-0.43/tracing-detail) >= 0.43.0
Provides:       crate(%{pkgname}/tracing-detail) = %{version}

%description -n %{name}+tracing-detail
This metapackage enables feature "tracing-detail" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+verbose-object-parsing-errors
Summary:        Interact with git repositories just like git would - feature "verbose-object-parsing-errors"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gix-object-0.50/verbose-object-parsing-errors) >= 0.50.0
Provides:       crate(%{pkgname}/verbose-object-parsing-errors) = %{version}

%description -n %{name}+verbose-object-parsing-errors
This metapackage enables feature "verbose-object-parsing-errors" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+worktree-archive
Summary:        Interact with git repositories just like git would - feature "worktree-archive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/attributes) = %{version}
Requires:       crate(%{pkgname}/gix-archive) = %{version}
Requires:       crate(%{pkgname}/worktree-stream) = %{version}
Provides:       crate(%{pkgname}/worktree-archive) = %{version}

%description -n %{name}+worktree-archive
This metapackage enables feature "worktree-archive" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+worktree-mutation
Summary:        Interact with git repositories just like git would - feature "worktree-mutation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/attributes) = %{version}
Requires:       crate(gix-worktree-state-0.20/default) >= 0.20.0
Provides:       crate(%{pkgname}/worktree-mutation) = %{version}

%description -n %{name}+worktree-mutation
This metapackage enables feature "worktree-mutation" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+worktree-stream
Summary:        Interact with git repositories just like git would - feature "worktree-stream"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/attributes) = %{version}
Requires:       crate(%{pkgname}/gix-worktree-stream) = %{version}
Provides:       crate(%{pkgname}/worktree-stream) = %{version}

%description -n %{name}+worktree-stream
This metapackage enables feature "worktree-stream" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zlib-ng
Summary:        Interact with git repositories just like git would - feature "zlib-ng" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(gix-features-0.43/once-cell) >= 0.43.0
Requires:       crate(gix-features-0.43/progress) >= 0.43.0
Requires:       crate(gix-features-0.43/zlib) >= 0.43.0
Provides:       crate(%{pkgname}/zlib-ng) = %{version}
Provides:       crate(%{pkgname}/zlib-ng-compat) = %{version}
Provides:       crate(%{pkgname}/zlib-rs) = %{version}
Provides:       crate(%{pkgname}/zlib-stock) = %{version}

%description -n %{name}+zlib-ng
This metapackage enables feature "zlib-ng" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "zlib-ng-compat", "zlib-rs", and "zlib-stock" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
