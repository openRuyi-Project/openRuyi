# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
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
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(gix-actor-0.35/default) >= 0.35.6
Requires:       crate(gix-commitgraph-0.29/default) >= 0.29.0
Requires:       crate(gix-config-0.46/default) >= 0.46.0
Requires:       crate(gix-date-0.10/default) >= 0.10.7
Requires:       crate(gix-diff-0.53) >= 0.53.0
Requires:       crate(gix-discover-0.41/default) >= 0.41.0
Requires:       crate(gix-features-0.43/default) >= 0.43.1
Requires:       crate(gix-features-0.43/once-cell) >= 0.43.1
Requires:       crate(gix-features-0.43/progress) >= 0.43.1
Requires:       crate(gix-fs-0.16/default) >= 0.16.1
Requires:       crate(gix-glob-0.21/default) >= 0.21.0
Requires:       crate(gix-hash-0.19/default) >= 0.19.0
Requires:       crate(gix-hashtable-0.9/default) >= 0.9.0
Requires:       crate(gix-lock-18.0/default) >= 18.0.0
Requires:       crate(gix-object-0.50/default) >= 0.50.2
Requires:       crate(gix-odb-0.70/default) >= 0.70.0
Requires:       crate(gix-pack-0.60/object-cache-dynamic) >= 0.60.0
Requires:       crate(gix-path-0.10/default) >= 0.10.22
Requires:       crate(gix-protocol-0.51/default) >= 0.51.0
Requires:       crate(gix-ref-0.53/default) >= 0.53.1
Requires:       crate(gix-refspec-0.31/default) >= 0.31.0
Requires:       crate(gix-revision-0.35) >= 0.35.0
Requires:       crate(gix-revwalk-0.21/default) >= 0.21.0
Requires:       crate(gix-sec-0.12/default) >= 0.12.2
Requires:       crate(gix-shallow-0.5/default) >= 0.5.0
Requires:       crate(gix-tempfile-18.0) >= 18.0.0
Requires:       crate(gix-trace-0.1/default) >= 0.1.18
Requires:       crate(gix-traverse-0.47/default) >= 0.47.0
Requires:       crate(gix-url-0.32/default) >= 0.32.0
Requires:       crate(gix-utils-0.3/default) >= 0.3.1
Requires:       crate(gix-validate-0.10/default) >= 0.10.1
Requires:       crate(once-cell-1.0/default) >= 1.21.4
Requires:       crate(smallvec-1.0/default) >= 1.15.1
Requires:       crate(thiserror-2.0/default) >= 2.0.18
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/tree-editor)

%description
Source code for takopackized Rust crate "gix"

%package     -n %{name}+async-network-client
Summary:        Interact with git repositories just like git would - feature "async-network-client"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/attributes)
Requires:       crate(%{pkgname}/credentials)
Requires:       crate(gix-pack-0.60/object-cache-dynamic) >= 0.60.0
Requires:       crate(gix-pack-0.60/streaming-input) >= 0.60.0
Requires:       crate(gix-protocol-0.51/async-client) >= 0.51.0
Requires:       crate(gix-transport-0.48/default) >= 0.48.0
Provides:       crate(%{pkgname}/async-network-client)

%description -n %{name}+async-network-client
This metapackage enables feature "async-network-client" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-network-client-async-std
Summary:        Interact with git repositories just like git would - feature "async-network-client-async-std"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/async-network-client)
Requires:       crate(%{pkgname}/async-std)
Requires:       crate(gix-transport-0.48/async-std) >= 0.48.0
Provides:       crate(%{pkgname}/async-network-client-async-std)

%description -n %{name}+async-network-client-async-std
This metapackage enables feature "async-network-client-async-std" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-std
Summary:        Interact with git repositories just like git would - feature "async-std"
Requires:       crate(%{pkgname})
Requires:       crate(async-std-1.0/default) >= 1.12.0
Provides:       crate(%{pkgname}/async-std)

%description -n %{name}+async-std
This metapackage enables feature "async-std" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+attributes
Summary:        Interact with git repositories just like git would - feature "attributes"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/command)
Requires:       crate(%{pkgname}/excludes)
Requires:       crate(gix-attributes-0.27/default) >= 0.27.0
Requires:       crate(gix-filter-0.20/default) >= 0.20.0
Requires:       crate(gix-pathspec-0.12/default) >= 0.12.0
Requires:       crate(gix-submodule-0.20/default) >= 0.20.0
Requires:       crate(gix-worktree-0.42/attributes) >= 0.42.0
Provides:       crate(%{pkgname}/attributes)

%description -n %{name}+attributes
This metapackage enables feature "attributes" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+basic
Summary:        Interact with git repositories just like git would - feature "basic"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/blob-diff)
Requires:       crate(%{pkgname}/index)
Requires:       crate(%{pkgname}/revision)
Provides:       crate(%{pkgname}/basic)

%description -n %{name}+basic
This metapackage enables feature "basic" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blame
Summary:        Interact with git repositories just like git would - feature "blame"
Requires:       crate(%{pkgname})
Requires:       crate(gix-blame-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/blame)

%description -n %{name}+blame
This metapackage enables feature "blame" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blob-diff
Summary:        Interact with git repositories just like git would - feature "blob-diff"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/attributes)
Requires:       crate(gix-diff-0.53/blob) >= 0.53.0
Provides:       crate(%{pkgname}/blob-diff)

%description -n %{name}+blob-diff
This metapackage enables feature "blob-diff" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blocking-http-transport-curl
Summary:        Interact with git repositories just like git would - feature "blocking-http-transport-curl"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/blocking-network-client)
Requires:       crate(gix-transport-0.48/http-client-curl) >= 0.48.0
Provides:       crate(%{pkgname}/blocking-http-transport-curl)

%description -n %{name}+blocking-http-transport-curl
This metapackage enables feature "blocking-http-transport-curl" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blocking-http-transport-curl-rustls
Summary:        Interact with git repositories just like git would - feature "blocking-http-transport-curl-rustls"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/blocking-http-transport-curl)
Requires:       crate(gix-transport-0.48/http-client-curl-rust-tls) >= 0.48.0
Provides:       crate(%{pkgname}/blocking-http-transport-curl-rustls)

%description -n %{name}+blocking-http-transport-curl-rustls
This metapackage enables feature "blocking-http-transport-curl-rustls" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blocking-http-transport-reqwest
Summary:        Interact with git repositories just like git would - feature "blocking-http-transport-reqwest"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/blocking-network-client)
Requires:       crate(gix-transport-0.48/http-client-reqwest) >= 0.48.0
Provides:       crate(%{pkgname}/blocking-http-transport-reqwest)

%description -n %{name}+blocking-http-transport-reqwest
This metapackage enables feature "blocking-http-transport-reqwest" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blocking-http-transport-reqwest-native-tls
Summary:        Interact with git repositories just like git would - feature "blocking-http-transport-reqwest-native-tls"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/blocking-http-transport-reqwest)
Requires:       crate(gix-transport-0.48/http-client-reqwest-native-tls) >= 0.48.0
Provides:       crate(%{pkgname}/blocking-http-transport-reqwest-native-tls)

%description -n %{name}+blocking-http-transport-reqwest-native-tls
This metapackage enables feature "blocking-http-transport-reqwest-native-tls" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blocking-http-transport-reqwest-rust-tls
Summary:        Interact with git repositories just like git would - feature "blocking-http-transport-reqwest-rust-tls"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/blocking-http-transport-reqwest)
Requires:       crate(gix-transport-0.48/http-client-reqwest-rust-tls) >= 0.48.0
Provides:       crate(%{pkgname}/blocking-http-transport-reqwest-rust-tls)

%description -n %{name}+blocking-http-transport-reqwest-rust-tls
This metapackage enables feature "blocking-http-transport-reqwest-rust-tls" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blocking-http-transport-reqwest-rust-tls-trust-dns
Summary:        Interact with git repositories just like git would - feature "blocking-http-transport-reqwest-rust-tls-trust-dns"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/blocking-http-transport-reqwest)
Requires:       crate(gix-transport-0.48/http-client-reqwest-rust-tls-trust-dns) >= 0.48.0
Provides:       crate(%{pkgname}/blocking-http-transport-reqwest-rust-tls-trust-dns)

%description -n %{name}+blocking-http-transport-reqwest-rust-tls-trust-dns
This metapackage enables feature "blocking-http-transport-reqwest-rust-tls-trust-dns" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+blocking-network-client
Summary:        Interact with git repositories just like git would - feature "blocking-network-client"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/attributes)
Requires:       crate(%{pkgname}/credentials)
Requires:       crate(gix-pack-0.60/object-cache-dynamic) >= 0.60.0
Requires:       crate(gix-pack-0.60/streaming-input) >= 0.60.0
Requires:       crate(gix-protocol-0.51/blocking-client) >= 0.51.0
Requires:       crate(gix-transport-0.48/default) >= 0.48.0
Provides:       crate(%{pkgname}/blocking-network-client)

%description -n %{name}+blocking-network-client
This metapackage enables feature "blocking-network-client" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cache-efficiency-debug
Summary:        Interact with git repositories just like git would - feature "cache-efficiency-debug"
Requires:       crate(%{pkgname})
Requires:       crate(gix-features-0.43/cache-efficiency-debug) >= 0.43.1
Requires:       crate(gix-features-0.43/once-cell) >= 0.43.1
Requires:       crate(gix-features-0.43/progress) >= 0.43.1
Provides:       crate(%{pkgname}/cache-efficiency-debug)

%description -n %{name}+cache-efficiency-debug
This metapackage enables feature "cache-efficiency-debug" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+comfort
Summary:        Interact with git repositories just like git would - feature "comfort"
Requires:       crate(%{pkgname})
Requires:       crate(gix-features-0.43/once-cell) >= 0.43.1
Requires:       crate(gix-features-0.43/progress) >= 0.43.1
Requires:       crate(gix-features-0.43/progress-unit-bytes) >= 0.43.1
Requires:       crate(gix-features-0.43/progress-unit-human-numbers) >= 0.43.1
Provides:       crate(%{pkgname}/comfort)

%description -n %{name}+comfort
This metapackage enables feature "comfort" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+command
Summary:        Interact with git repositories just like git would - feature "command"
Requires:       crate(%{pkgname})
Requires:       crate(gix-command-0.6/default) >= 0.6.5
Provides:       crate(%{pkgname}/command)

%description -n %{name}+command
This metapackage enables feature "command" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+credentials
Summary:        Interact with git repositories just like git would - feature "credentials"
Requires:       crate(%{pkgname})
Requires:       crate(gix-credentials-0.30/default) >= 0.30.0
Requires:       crate(gix-negotiate-0.21/default) >= 0.21.0
Requires:       crate(gix-prompt-0.11/default) >= 0.11.2
Provides:       crate(%{pkgname}/credentials)

%description -n %{name}+credentials
This metapackage enables feature "credentials" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Interact with git repositories just like git would - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/basic)
Requires:       crate(%{pkgname}/comfort)
Requires:       crate(%{pkgname}/extras)
Requires:       crate(%{pkgname}/max-performance-safe)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dirwalk
Summary:        Interact with git repositories just like git would - feature "dirwalk"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/attributes)
Requires:       crate(%{pkgname}/excludes)
Requires:       crate(gix-dir-0.15/default) >= 0.15.0
Provides:       crate(%{pkgname}/dirwalk)

%description -n %{name}+dirwalk
This metapackage enables feature "dirwalk" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+document-features
Summary:        Interact with git repositories just like git would - feature "document-features"
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/document-features)

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+excludes
Summary:        Interact with git repositories just like git would - feature "excludes"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/index)
Requires:       crate(gix-ignore-0.16/default) >= 0.16.0
Requires:       crate(gix-worktree-0.42) >= 0.42.0
Provides:       crate(%{pkgname}/excludes)

%description -n %{name}+excludes
This metapackage enables feature "excludes" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+extras
Summary:        Interact with git repositories just like git would - feature "extras"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/attributes)
Requires:       crate(%{pkgname}/credentials)
Requires:       crate(%{pkgname}/dirwalk)
Requires:       crate(%{pkgname}/excludes)
Requires:       crate(%{pkgname}/interrupt)
Requires:       crate(%{pkgname}/mailmap)
Requires:       crate(%{pkgname}/revparse-regex)
Requires:       crate(%{pkgname}/status)
Requires:       crate(%{pkgname}/worktree-archive)
Requires:       crate(%{pkgname}/worktree-mutation)
Requires:       crate(%{pkgname}/worktree-stream)
Provides:       crate(%{pkgname}/extras)

%description -n %{name}+extras
This metapackage enables feature "extras" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gix-archive
Summary:        Interact with git repositories just like git would - feature "gix-archive"
Requires:       crate(%{pkgname})
Requires:       crate(gix-archive-0.22) >= 0.22.0
Provides:       crate(%{pkgname}/gix-archive)

%description -n %{name}+gix-archive
This metapackage enables feature "gix-archive" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gix-status
Summary:        Interact with git repositories just like git would - feature "gix-status"
Requires:       crate(%{pkgname})
Requires:       crate(gix-status-0.20/default) >= 0.20.0
Requires:       crate(gix-status-0.20/worktree-rewrites) >= 0.20.0
Provides:       crate(%{pkgname}/gix-status)

%description -n %{name}+gix-status
This metapackage enables feature "gix-status" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gix-worktree-stream
Summary:        Interact with git repositories just like git would - feature "gix-worktree-stream"
Requires:       crate(%{pkgname})
Requires:       crate(gix-worktree-stream-0.22/default) >= 0.22.0
Provides:       crate(%{pkgname}/gix-worktree-stream)

%description -n %{name}+gix-worktree-stream
This metapackage enables feature "gix-worktree-stream" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hp-tempfile-registry
Summary:        Interact with git repositories just like git would - feature "hp-tempfile-registry"
Requires:       crate(%{pkgname})
Requires:       crate(gix-tempfile-18.0/hp-hashmap) >= 18.0.0
Provides:       crate(%{pkgname}/hp-tempfile-registry)

%description -n %{name}+hp-tempfile-registry
This metapackage enables feature "hp-tempfile-registry" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+index
Summary:        Interact with git repositories just like git would - feature "index"
Requires:       crate(%{pkgname})
Requires:       crate(gix-index-0.41/default) >= 0.41.0
Provides:       crate(%{pkgname}/index)

%description -n %{name}+index
This metapackage enables feature "index" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+interrupt
Summary:        Interact with git repositories just like git would - feature "interrupt"
Requires:       crate(%{pkgname})
Requires:       crate(gix-tempfile-18.0/signals) >= 18.0.0
Requires:       crate(parking-lot-0.12/default) >= 0.12.4
Requires:       crate(signal-hook-0.3) >= 0.3.18
Provides:       crate(%{pkgname}/interrupt)

%description -n %{name}+interrupt
This metapackage enables feature "interrupt" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mailmap
Summary:        Interact with git repositories just like git would - feature "mailmap"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/revision)
Requires:       crate(gix-mailmap-0.27/default) >= 0.27.2
Provides:       crate(%{pkgname}/mailmap)

%description -n %{name}+mailmap
This metapackage enables feature "mailmap" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+max-control
Summary:        Interact with git repositories just like git would - feature "max-control" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/pack-cache-lru-dynamic)
Requires:       crate(%{pkgname}/pack-cache-lru-static)
Requires:       crate(%{pkgname}/parallel)
Provides:       crate(%{pkgname}/max-control)
Provides:       crate(%{pkgname}/max-performance)
Provides:       crate(%{pkgname}/max-performance-safe)

%description -n %{name}+max-control
This metapackage enables feature "max-control" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "max-performance", and "max-performance-safe" features.

%package     -n %{name}+merge
Summary:        Interact with git repositories just like git would - feature "merge"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/attributes)
Requires:       crate(%{pkgname}/blob-diff)
Requires:       crate(%{pkgname}/tree-editor)
Requires:       crate(gix-merge-0.6) >= 0.6.0
Provides:       crate(%{pkgname}/merge)

%description -n %{name}+merge
This metapackage enables feature "merge" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+need-more-recent-msrv
Summary:        Interact with git repositories just like git would - feature "need-more-recent-msrv"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/merge)
Requires:       crate(%{pkgname}/tree-editor)
Provides:       crate(%{pkgname}/need-more-recent-msrv)

%description -n %{name}+need-more-recent-msrv
This metapackage enables feature "need-more-recent-msrv" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pack-cache-lru-dynamic
Summary:        Interact with git repositories just like git would - feature "pack-cache-lru-dynamic"
Requires:       crate(%{pkgname})
Requires:       crate(gix-pack-0.60/object-cache-dynamic) >= 0.60.0
Requires:       crate(gix-pack-0.60/pack-cache-lru-dynamic) >= 0.60.0
Provides:       crate(%{pkgname}/pack-cache-lru-dynamic)

%description -n %{name}+pack-cache-lru-dynamic
This metapackage enables feature "pack-cache-lru-dynamic" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pack-cache-lru-static
Summary:        Interact with git repositories just like git would - feature "pack-cache-lru-static"
Requires:       crate(%{pkgname})
Requires:       crate(gix-pack-0.60/object-cache-dynamic) >= 0.60.0
Requires:       crate(gix-pack-0.60/pack-cache-lru-static) >= 0.60.0
Provides:       crate(%{pkgname}/pack-cache-lru-static)

%description -n %{name}+pack-cache-lru-static
This metapackage enables feature "pack-cache-lru-static" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+parallel
Summary:        Interact with git repositories just like git would - feature "parallel"
Requires:       crate(%{pkgname})
Requires:       crate(gix-features-0.43/once-cell) >= 0.43.1
Requires:       crate(gix-features-0.43/parallel) >= 0.43.1
Requires:       crate(gix-features-0.43/progress) >= 0.43.1
Provides:       crate(%{pkgname}/parallel)

%description -n %{name}+parallel
This metapackage enables feature "parallel" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+prodash
Summary:        Interact with git repositories just like git would - feature "prodash"
Requires:       crate(%{pkgname})
Requires:       crate(prodash-30.0/default) >= 30.0.1
Requires:       crate(prodash-30.0/progress-tree) >= 30.0.1
Provides:       crate(%{pkgname}/prodash)

%description -n %{name}+prodash
This metapackage enables feature "prodash" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+progress-tree
Summary:        Interact with git repositories just like git would - feature "progress-tree"
Requires:       crate(%{pkgname})
Requires:       crate(prodash-30.0/progress-tree) >= 30.0.1
Provides:       crate(%{pkgname}/progress-tree)

%description -n %{name}+progress-tree
This metapackage enables feature "progress-tree" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+regex
Summary:        Interact with git repositories just like git would - feature "regex"
Requires:       crate(%{pkgname})
Requires:       crate(regex-1.0/std) >= 1.6.0
Provides:       crate(%{pkgname}/regex)

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+revision
Summary:        Interact with git repositories just like git would - feature "revision"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/index)
Requires:       crate(gix-revision-0.35/describe) >= 0.35.0
Requires:       crate(gix-revision-0.35/merge-base) >= 0.35.0
Provides:       crate(%{pkgname}/revision)

%description -n %{name}+revision
This metapackage enables feature "revision" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+revparse-regex
Summary:        Interact with git repositories just like git would - feature "revparse-regex"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/regex)
Requires:       crate(%{pkgname}/revision)
Provides:       crate(%{pkgname}/revparse-regex)

%description -n %{name}+revparse-regex
This metapackage enables feature "revparse-regex" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Interact with git repositories just like git would - feature "serde"
Requires:       crate(%{pkgname})
Requires:       crate(gix-attributes-0.27/serde) >= 0.27.0
Requires:       crate(gix-commitgraph-0.29/serde) >= 0.29.0
Requires:       crate(gix-credentials-0.30/serde) >= 0.30.0
Requires:       crate(gix-ignore-0.16/serde) >= 0.16.0
Requires:       crate(gix-index-0.41/serde) >= 0.41.0
Requires:       crate(gix-mailmap-0.27/serde) >= 0.27.2
Requires:       crate(gix-object-0.50/serde) >= 0.50.2
Requires:       crate(gix-odb-0.70/serde) >= 0.70.0
Requires:       crate(gix-pack-0.60/object-cache-dynamic) >= 0.60.0
Requires:       crate(gix-pack-0.60/serde) >= 0.60.0
Requires:       crate(gix-protocol-0.51/serde) >= 0.51.0
Requires:       crate(gix-ref-0.53/serde) >= 0.53.1
Requires:       crate(gix-revision-0.35/serde) >= 0.35.0
Requires:       crate(gix-transport-0.48/serde) >= 0.48.0
Requires:       crate(gix-url-0.32/serde) >= 0.32.0
Requires:       crate(gix-worktree-0.42/serde) >= 0.42.0
Requires:       crate(serde-1.0/derive) >= 1.0.114
Provides:       crate(%{pkgname}/serde)

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+status
Summary:        Interact with git repositories just like git would - feature "status"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/blob-diff)
Requires:       crate(%{pkgname}/dirwalk)
Requires:       crate(%{pkgname}/gix-status)
Requires:       crate(%{pkgname}/index)
Requires:       crate(gix-diff-0.53/index) >= 0.53.0
Provides:       crate(%{pkgname}/status)

%description -n %{name}+status
This metapackage enables feature "status" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing
Summary:        Interact with git repositories just like git would - feature "tracing"
Requires:       crate(%{pkgname})
Requires:       crate(gix-features-0.43/once-cell) >= 0.43.1
Requires:       crate(gix-features-0.43/progress) >= 0.43.1
Requires:       crate(gix-features-0.43/tracing) >= 0.43.1
Provides:       crate(%{pkgname}/tracing)

%description -n %{name}+tracing
This metapackage enables feature "tracing" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tracing-detail
Summary:        Interact with git repositories just like git would - feature "tracing-detail"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/tracing)
Requires:       crate(gix-features-0.43/once-cell) >= 0.43.1
Requires:       crate(gix-features-0.43/progress) >= 0.43.1
Requires:       crate(gix-features-0.43/tracing-detail) >= 0.43.1
Provides:       crate(%{pkgname}/tracing-detail)

%description -n %{name}+tracing-detail
This metapackage enables feature "tracing-detail" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+verbose-object-parsing-errors
Summary:        Interact with git repositories just like git would - feature "verbose-object-parsing-errors"
Requires:       crate(%{pkgname})
Requires:       crate(gix-object-0.50/verbose-object-parsing-errors) >= 0.50.2
Provides:       crate(%{pkgname}/verbose-object-parsing-errors)

%description -n %{name}+verbose-object-parsing-errors
This metapackage enables feature "verbose-object-parsing-errors" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+worktree-archive
Summary:        Interact with git repositories just like git would - feature "worktree-archive"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/attributes)
Requires:       crate(%{pkgname}/gix-archive)
Requires:       crate(%{pkgname}/worktree-stream)
Provides:       crate(%{pkgname}/worktree-archive)

%description -n %{name}+worktree-archive
This metapackage enables feature "worktree-archive" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+worktree-mutation
Summary:        Interact with git repositories just like git would - feature "worktree-mutation"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/attributes)
Requires:       crate(gix-worktree-state-0.20/default) >= 0.20.0
Provides:       crate(%{pkgname}/worktree-mutation)

%description -n %{name}+worktree-mutation
This metapackage enables feature "worktree-mutation" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+worktree-stream
Summary:        Interact with git repositories just like git would - feature "worktree-stream"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/attributes)
Requires:       crate(%{pkgname}/gix-worktree-stream)
Provides:       crate(%{pkgname}/worktree-stream)

%description -n %{name}+worktree-stream
This metapackage enables feature "worktree-stream" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zlib-ng
Summary:        Interact with git repositories just like git would - feature "zlib-ng" and 3 more
Requires:       crate(%{pkgname})
Requires:       crate(gix-features-0.43/once-cell) >= 0.43.1
Requires:       crate(gix-features-0.43/progress) >= 0.43.1
Requires:       crate(gix-features-0.43/zlib) >= 0.43.1
Provides:       crate(%{pkgname}/zlib-ng)
Provides:       crate(%{pkgname}/zlib-ng-compat)
Provides:       crate(%{pkgname}/zlib-rs)
Provides:       crate(%{pkgname}/zlib-stock)

%description -n %{name}+zlib-ng
This metapackage enables feature "zlib-ng" for the Rust gix crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "zlib-ng-compat", "zlib-rs", and "zlib-stock" features.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
