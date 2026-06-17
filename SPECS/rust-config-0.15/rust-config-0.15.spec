# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name config
%global full_version 0.15.18
%global pkgname config-0.15

Name:           rust-config-0.15
Version:        0.15.18
Release:        %autorelease
Summary:        Rust crate "config"
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-cli/config-rs
#!RemoteAsset:  sha256:180e549344080374f9b32ed41bf3b6b57885ff6a289367b3dbc10eea8acc1918
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(pathdiff-0.2/default) >= 0.2.3
Requires:       crate(serde-core-1/default) >= 1.0.226
Requires:       crate(winnow-0.7/default) >= 0.7.13
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "config"

%package     -n %{name}+async-trait
Summary:        Layered configuration system for Rust applications - feature "async-trait" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(async-trait-0.1/default) >= 0.1.89
Provides:       crate(%{pkgname}/async) = %{version}
Provides:       crate(%{pkgname}/async-trait) = %{version}

%description -n %{name}+async-trait
This metapackage enables feature "async-trait" for the Rust config crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "async" feature.

%package     -n %{name}+convert-case
Summary:        Layered configuration system for Rust applications - feature "convert_case"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(convert-case-0.6/default) >= 0.6.0
Provides:       crate(%{pkgname}/convert-case) = %{version}

%description -n %{name}+convert-case
This metapackage enables feature "convert_case" for the Rust config crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+corn
Summary:        Layered configuration system for Rust applications - feature "corn"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libcorn-0.10/default) >= 0.10.0
Provides:       crate(%{pkgname}/corn) = %{version}

%description -n %{name}+corn
This metapackage enables feature "corn" for the Rust config crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Layered configuration system for Rust applications - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async) = %{version}
Requires:       crate(%{pkgname}/convert-case) = %{version}
Requires:       crate(%{pkgname}/ini) = %{version}
Requires:       crate(%{pkgname}/json) = %{version}
Requires:       crate(%{pkgname}/json5) = %{version}
Requires:       crate(%{pkgname}/ron) = %{version}
Requires:       crate(%{pkgname}/toml) = %{version}
Requires:       crate(%{pkgname}/yaml) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust config crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+indexmap
Summary:        Layered configuration system for Rust applications - feature "indexmap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-2/default) >= 2.11.4
Requires:       crate(indexmap-2/serde) >= 2.11.4
Provides:       crate(%{pkgname}/indexmap) = %{version}

%description -n %{name}+indexmap
This metapackage enables feature "indexmap" for the Rust config crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+json5
Summary:        Layered configuration system for Rust applications - feature "json5"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/json5-rs) = %{version}
Requires:       crate(serde-untagged-0.1/default) >= 0.1.9
Provides:       crate(%{pkgname}/json5) = %{version}

%description -n %{name}+json5
This metapackage enables feature "json5" for the Rust config crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+json5-rs
Summary:        Layered configuration system for Rust applications - feature "json5_rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(json5-0.4/default) >= 0.4.1
Provides:       crate(%{pkgname}/json5-rs) = %{version}

%description -n %{name}+json5-rs
This metapackage enables feature "json5_rs" for the Rust config crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+preserve-order
Summary:        Layered configuration system for Rust applications - feature "preserve_order"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/indexmap) = %{version}
Requires:       crate(ron-0.8/indexmap) >= 0.8.1
Requires:       crate(serde-json-1/preserve-order) >= 1.0.145
Requires:       crate(toml-0.9/parse) >= 0.9.6
Requires:       crate(toml-0.9/preserve-order) >= 0.9.6
Requires:       crate(toml-0.9/serde) >= 0.9.6
Provides:       crate(%{pkgname}/preserve-order) = %{version}

%description -n %{name}+preserve-order
This metapackage enables feature "preserve_order" for the Rust config crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ron
Summary:        Layered configuration system for Rust applications - feature "ron"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(ron-0.8/default) >= 0.8.1
Provides:       crate(%{pkgname}/ron) = %{version}

%description -n %{name}+ron
This metapackage enables feature "ron" for the Rust config crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rust-ini
Summary:        Layered configuration system for Rust applications - feature "rust-ini" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rust-ini-0.21/default) >= 0.21.3
Provides:       crate(%{pkgname}/ini) = %{version}
Provides:       crate(%{pkgname}/rust-ini) = %{version}

%description -n %{name}+rust-ini
This metapackage enables feature "rust-ini" for the Rust config crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "ini" feature.

%package     -n %{name}+serde-json
Summary:        Layered configuration system for Rust applications - feature "serde_json" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-json-1/default) >= 1.0.145
Provides:       crate(%{pkgname}/json) = %{version}
Provides:       crate(%{pkgname}/serde-json) = %{version}

%description -n %{name}+serde-json
This metapackage enables feature "serde_json" for the Rust config crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "json" feature.

%package     -n %{name}+toml
Summary:        Layered configuration system for Rust applications - feature "toml"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(toml-0.9/parse) >= 0.9.6
Requires:       crate(toml-0.9/serde) >= 0.9.6
Provides:       crate(%{pkgname}/toml) = %{version}

%description -n %{name}+toml
This metapackage enables feature "toml" for the Rust config crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+yaml-rust2
Summary:        Layered configuration system for Rust applications - feature "yaml-rust2" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(yaml-rust2-0.10/default) >= 0.10.4
Provides:       crate(%{pkgname}/yaml) = %{version}
Provides:       crate(%{pkgname}/yaml-rust2) = %{version}

%description -n %{name}+yaml-rust2
This metapackage enables feature "yaml-rust2" for the Rust config crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "yaml" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
