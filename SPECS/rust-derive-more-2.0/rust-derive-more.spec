# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name derive_more
%global full_version 2.1.1
%global pkgname derive-more-2.0

Name:           rust-derive-more-2.0
Version:        2.1.1
Release:        %autorelease
Summary:        Rust crate "derive_more"
License:        MIT
URL:            https://github.com/JelteF/derive_more
#!RemoteAsset:  sha256:d751e9e49156b02b44f9c1815bcb94b984cdcc4396ecc32521c739452808b134
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(derive-more-impl-2.0/default) >= 2.1.1
Provides:       crate(derive-more) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "derive_more"

%package     -n %{name}+add
Summary:        Adds #[derive(x)] macros for more traits - feature "add"
Requires:       crate(%{pkgname})
Requires:       crate(derive-more-impl-2.0/add) >= 2.1.1
Provides:       crate(%{pkgname}/add)

%description -n %{name}+add
This metapackage enables feature "add" for the Rust derive_more crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+add-assign
Summary:        Adds #[derive(x)] macros for more traits - feature "add_assign"
Requires:       crate(%{pkgname})
Requires:       crate(derive-more-impl-2.0/add-assign) >= 2.1.1
Provides:       crate(%{pkgname}/add-assign)

%description -n %{name}+add-assign
This metapackage enables feature "add_assign" for the Rust derive_more crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+as-ref
Summary:        Adds #[derive(x)] macros for more traits - feature "as_ref"
Requires:       crate(%{pkgname})
Requires:       crate(derive-more-impl-2.0/as-ref) >= 2.1.1
Provides:       crate(%{pkgname}/as-ref)

%description -n %{name}+as-ref
This metapackage enables feature "as_ref" for the Rust derive_more crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+constructor
Summary:        Adds #[derive(x)] macros for more traits - feature "constructor"
Requires:       crate(%{pkgname})
Requires:       crate(derive-more-impl-2.0/constructor) >= 2.1.1
Provides:       crate(%{pkgname}/constructor)

%description -n %{name}+constructor
This metapackage enables feature "constructor" for the Rust derive_more crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+debug
Summary:        Adds #[derive(x)] macros for more traits - feature "debug"
Requires:       crate(%{pkgname})
Requires:       crate(derive-more-impl-2.0/debug) >= 2.1.1
Provides:       crate(%{pkgname}/debug)

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust derive_more crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deref
Summary:        Adds #[derive(x)] macros for more traits - feature "deref"
Requires:       crate(%{pkgname})
Requires:       crate(derive-more-impl-2.0/deref) >= 2.1.1
Provides:       crate(%{pkgname}/deref)

%description -n %{name}+deref
This metapackage enables feature "deref" for the Rust derive_more crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+deref-mut
Summary:        Adds #[derive(x)] macros for more traits - feature "deref_mut"
Requires:       crate(%{pkgname})
Requires:       crate(derive-more-impl-2.0/deref-mut) >= 2.1.1
Provides:       crate(%{pkgname}/deref-mut)

%description -n %{name}+deref-mut
This metapackage enables feature "deref_mut" for the Rust derive_more crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+display
Summary:        Adds #[derive(x)] macros for more traits - feature "display"
Requires:       crate(%{pkgname})
Requires:       crate(derive-more-impl-2.0/display) >= 2.1.1
Provides:       crate(%{pkgname}/display)

%description -n %{name}+display
This metapackage enables feature "display" for the Rust derive_more crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+eq
Summary:        Adds #[derive(x)] macros for more traits - feature "eq"
Requires:       crate(%{pkgname})
Requires:       crate(derive-more-impl-2.0/eq) >= 2.1.1
Provides:       crate(%{pkgname}/eq)

%description -n %{name}+eq
This metapackage enables feature "eq" for the Rust derive_more crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+error
Summary:        Adds #[derive(x)] macros for more traits - feature "error"
Requires:       crate(%{pkgname})
Requires:       crate(derive-more-impl-2.0/error) >= 2.1.1
Provides:       crate(%{pkgname}/error)

%description -n %{name}+error
This metapackage enables feature "error" for the Rust derive_more crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+from
Summary:        Adds #[derive(x)] macros for more traits - feature "from"
Requires:       crate(%{pkgname})
Requires:       crate(derive-more-impl-2.0/from) >= 2.1.1
Provides:       crate(%{pkgname}/from)

%description -n %{name}+from
This metapackage enables feature "from" for the Rust derive_more crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+from-str
Summary:        Adds #[derive(x)] macros for more traits - feature "from_str"
Requires:       crate(%{pkgname})
Requires:       crate(derive-more-impl-2.0/from-str) >= 2.1.1
Provides:       crate(%{pkgname}/from-str)

%description -n %{name}+from-str
This metapackage enables feature "from_str" for the Rust derive_more crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+full
Summary:        Adds #[derive(x)] macros for more traits - feature "full"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/add)
Requires:       crate(%{pkgname}/add-assign)
Requires:       crate(%{pkgname}/as-ref)
Requires:       crate(%{pkgname}/constructor)
Requires:       crate(%{pkgname}/debug)
Requires:       crate(%{pkgname}/deref)
Requires:       crate(%{pkgname}/deref-mut)
Requires:       crate(%{pkgname}/display)
Requires:       crate(%{pkgname}/eq)
Requires:       crate(%{pkgname}/error)
Requires:       crate(%{pkgname}/from)
Requires:       crate(%{pkgname}/from-str)
Requires:       crate(%{pkgname}/index)
Requires:       crate(%{pkgname}/index-mut)
Requires:       crate(%{pkgname}/into)
Requires:       crate(%{pkgname}/into-iterator)
Requires:       crate(%{pkgname}/is-variant)
Requires:       crate(%{pkgname}/mul)
Requires:       crate(%{pkgname}/mul-assign)
Requires:       crate(%{pkgname}/not)
Requires:       crate(%{pkgname}/sum)
Requires:       crate(%{pkgname}/try-from)
Requires:       crate(%{pkgname}/try-into)
Requires:       crate(%{pkgname}/try-unwrap)
Requires:       crate(%{pkgname}/unwrap)
Provides:       crate(%{pkgname}/full)

%description -n %{name}+full
This metapackage enables feature "full" for the Rust derive_more crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+index
Summary:        Adds #[derive(x)] macros for more traits - feature "index"
Requires:       crate(%{pkgname})
Requires:       crate(derive-more-impl-2.0/index) >= 2.1.1
Provides:       crate(%{pkgname}/index)

%description -n %{name}+index
This metapackage enables feature "index" for the Rust derive_more crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+index-mut
Summary:        Adds #[derive(x)] macros for more traits - feature "index_mut"
Requires:       crate(%{pkgname})
Requires:       crate(derive-more-impl-2.0/index-mut) >= 2.1.1
Provides:       crate(%{pkgname}/index-mut)

%description -n %{name}+index-mut
This metapackage enables feature "index_mut" for the Rust derive_more crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+into
Summary:        Adds #[derive(x)] macros for more traits - feature "into"
Requires:       crate(%{pkgname})
Requires:       crate(derive-more-impl-2.0/into) >= 2.1.1
Provides:       crate(%{pkgname}/into)

%description -n %{name}+into
This metapackage enables feature "into" for the Rust derive_more crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+into-iterator
Summary:        Adds #[derive(x)] macros for more traits - feature "into_iterator"
Requires:       crate(%{pkgname})
Requires:       crate(derive-more-impl-2.0/into-iterator) >= 2.1.1
Provides:       crate(%{pkgname}/into-iterator)

%description -n %{name}+into-iterator
This metapackage enables feature "into_iterator" for the Rust derive_more crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+is-variant
Summary:        Adds #[derive(x)] macros for more traits - feature "is_variant"
Requires:       crate(%{pkgname})
Requires:       crate(derive-more-impl-2.0/is-variant) >= 2.1.1
Provides:       crate(%{pkgname}/is-variant)

%description -n %{name}+is-variant
This metapackage enables feature "is_variant" for the Rust derive_more crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mul
Summary:        Adds #[derive(x)] macros for more traits - feature "mul"
Requires:       crate(%{pkgname})
Requires:       crate(derive-more-impl-2.0/mul) >= 2.1.1
Provides:       crate(%{pkgname}/mul)

%description -n %{name}+mul
This metapackage enables feature "mul" for the Rust derive_more crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mul-assign
Summary:        Adds #[derive(x)] macros for more traits - feature "mul_assign"
Requires:       crate(%{pkgname})
Requires:       crate(derive-more-impl-2.0/mul-assign) >= 2.1.1
Provides:       crate(%{pkgname}/mul-assign)

%description -n %{name}+mul-assign
This metapackage enables feature "mul_assign" for the Rust derive_more crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+not
Summary:        Adds #[derive(x)] macros for more traits - feature "not"
Requires:       crate(%{pkgname})
Requires:       crate(derive-more-impl-2.0/not) >= 2.1.1
Provides:       crate(%{pkgname}/not)

%description -n %{name}+not
This metapackage enables feature "not" for the Rust derive_more crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+sum
Summary:        Adds #[derive(x)] macros for more traits - feature "sum"
Requires:       crate(%{pkgname})
Requires:       crate(derive-more-impl-2.0/sum) >= 2.1.1
Provides:       crate(%{pkgname}/sum)

%description -n %{name}+sum
This metapackage enables feature "sum" for the Rust derive_more crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+testing-helpers
Summary:        Adds #[derive(x)] macros for more traits - feature "testing-helpers"
Requires:       crate(%{pkgname})
Requires:       crate(derive-more-impl-2.0/testing-helpers) >= 2.1.1
Requires:       crate(rustc-version-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/testing-helpers)

%description -n %{name}+testing-helpers
This metapackage enables feature "testing-helpers" for the Rust derive_more crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+try-from
Summary:        Adds #[derive(x)] macros for more traits - feature "try_from"
Requires:       crate(%{pkgname})
Requires:       crate(derive-more-impl-2.0/try-from) >= 2.1.1
Provides:       crate(%{pkgname}/try-from)

%description -n %{name}+try-from
This metapackage enables feature "try_from" for the Rust derive_more crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+try-into
Summary:        Adds #[derive(x)] macros for more traits - feature "try_into"
Requires:       crate(%{pkgname})
Requires:       crate(derive-more-impl-2.0/try-into) >= 2.1.1
Provides:       crate(%{pkgname}/try-into)

%description -n %{name}+try-into
This metapackage enables feature "try_into" for the Rust derive_more crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+try-unwrap
Summary:        Adds #[derive(x)] macros for more traits - feature "try_unwrap"
Requires:       crate(%{pkgname})
Requires:       crate(derive-more-impl-2.0/try-unwrap) >= 2.1.1
Provides:       crate(%{pkgname}/try-unwrap)

%description -n %{name}+try-unwrap
This metapackage enables feature "try_unwrap" for the Rust derive_more crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+unwrap
Summary:        Adds #[derive(x)] macros for more traits - feature "unwrap"
Requires:       crate(%{pkgname})
Requires:       crate(derive-more-impl-2.0/unwrap) >= 2.1.1
Provides:       crate(%{pkgname}/unwrap)

%description -n %{name}+unwrap
This metapackage enables feature "unwrap" for the Rust derive_more crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
