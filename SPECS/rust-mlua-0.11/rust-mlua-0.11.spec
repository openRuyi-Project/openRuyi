# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name mlua
%global full_version 0.11.6
%global pkgname mlua-0.11

Name:           rust-mlua-0.11
Version:        0.11.6
Release:        %autorelease
Summary:        Rust crate "mlua"
License:        MIT
URL:            https://github.com/mlua-rs/mlua
#!RemoteAsset:  sha256:ccd36acfa49ce6ee56d1307a061dd302c564eee757e6e4cd67eb4f7204846fab
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bstr-1/std) >= 1.0.0
Requires:       crate(either-1/default) >= 1.0.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(mlua-sys-0.10/default) >= 0.10.0
Requires:       crate(num-traits-0.2/default) >= 0.2.14
Requires:       crate(parking-lot-0.12/arc-lock) >= 0.12.0
Requires:       crate(parking-lot-0.12/default) >= 0.12.0
Requires:       crate(rustc-hash-2/default) >= 2.0.0
Requires:       crate(rustversion-1/default) >= 1.0.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/error-send) = %{version}
Provides:       crate(%{pkgname}/send) = %{version}

%description
Source code for takopackized Rust crate "mlua"

%package     -n %{name}+anyhow
Summary:        High level bindings to Lua 5.5/5.4/5.3/5.2/5.1 (including LuaJIT) and Luau with async/await features and support of writing native Lua modules in Rust - feature "anyhow"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/error-send) = %{version}
Requires:       crate(anyhow-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/anyhow) = %{version}

%description -n %{name}+anyhow
This metapackage enables feature "anyhow" for the Rust mlua crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async
Summary:        High level bindings to Lua 5.5/5.4/5.3/5.2/5.1 (including LuaJIT) and Luau with async/await features and support of writing native Lua modules in Rust - feature "async"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-util-0.3/std) >= 0.3.0
Provides:       crate(%{pkgname}/async) = %{version}

%description -n %{name}+async
This metapackage enables feature "async" for the Rust mlua crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lua51
Summary:        High level bindings to Lua 5.5/5.4/5.3/5.2/5.1 (including LuaJIT) and Luau with async/await features and support of writing native Lua modules in Rust - feature "lua51"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mlua-sys-0.10/lua51) >= 0.10.0
Provides:       crate(%{pkgname}/lua51) = %{version}

%description -n %{name}+lua51
This metapackage enables feature "lua51" for the Rust mlua crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lua52
Summary:        High level bindings to Lua 5.5/5.4/5.3/5.2/5.1 (including LuaJIT) and Luau with async/await features and support of writing native Lua modules in Rust - feature "lua52"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mlua-sys-0.10/lua52) >= 0.10.0
Provides:       crate(%{pkgname}/lua52) = %{version}

%description -n %{name}+lua52
This metapackage enables feature "lua52" for the Rust mlua crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lua53
Summary:        High level bindings to Lua 5.5/5.4/5.3/5.2/5.1 (including LuaJIT) and Luau with async/await features and support of writing native Lua modules in Rust - feature "lua53"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mlua-sys-0.10/lua53) >= 0.10.0
Provides:       crate(%{pkgname}/lua53) = %{version}

%description -n %{name}+lua53
This metapackage enables feature "lua53" for the Rust mlua crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lua54
Summary:        High level bindings to Lua 5.5/5.4/5.3/5.2/5.1 (including LuaJIT) and Luau with async/await features and support of writing native Lua modules in Rust - feature "lua54"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mlua-sys-0.10/lua54) >= 0.10.0
Provides:       crate(%{pkgname}/lua54) = %{version}

%description -n %{name}+lua54
This metapackage enables feature "lua54" for the Rust mlua crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+lua55
Summary:        High level bindings to Lua 5.5/5.4/5.3/5.2/5.1 (including LuaJIT) and Luau with async/await features and support of writing native Lua modules in Rust - feature "lua55"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mlua-sys-0.10/lua55) >= 0.10.0
Provides:       crate(%{pkgname}/lua55) = %{version}

%description -n %{name}+lua55
This metapackage enables feature "lua55" for the Rust mlua crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+luajit
Summary:        High level bindings to Lua 5.5/5.4/5.3/5.2/5.1 (including LuaJIT) and Luau with async/await features and support of writing native Lua modules in Rust - feature "luajit"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mlua-sys-0.10/luajit) >= 0.10.0
Provides:       crate(%{pkgname}/luajit) = %{version}

%description -n %{name}+luajit
This metapackage enables feature "luajit" for the Rust mlua crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+luajit52
Summary:        High level bindings to Lua 5.5/5.4/5.3/5.2/5.1 (including LuaJIT) and Luau with async/await features and support of writing native Lua modules in Rust - feature "luajit52"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/luajit) = %{version}
Requires:       crate(mlua-sys-0.10/luajit52) >= 0.10.0
Provides:       crate(%{pkgname}/luajit52) = %{version}

%description -n %{name}+luajit52
This metapackage enables feature "luajit52" for the Rust mlua crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+luau
Summary:        High level bindings to Lua 5.5/5.4/5.3/5.2/5.1 (including LuaJIT) and Luau with async/await features and support of writing native Lua modules in Rust - feature "luau"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mlua-sys-0.10/luau) >= 0.10.0
Provides:       crate(%{pkgname}/luau) = %{version}

%description -n %{name}+luau
This metapackage enables feature "luau" for the Rust mlua crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+luau-jit
Summary:        High level bindings to Lua 5.5/5.4/5.3/5.2/5.1 (including LuaJIT) and Luau with async/await features and support of writing native Lua modules in Rust - feature "luau-jit"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/luau) = %{version}
Requires:       crate(mlua-sys-0.10/luau-codegen) >= 0.10.0
Provides:       crate(%{pkgname}/luau-jit) = %{version}

%description -n %{name}+luau-jit
This metapackage enables feature "luau-jit" for the Rust mlua crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+luau-vector4
Summary:        High level bindings to Lua 5.5/5.4/5.3/5.2/5.1 (including LuaJIT) and Luau with async/await features and support of writing native Lua modules in Rust - feature "luau-vector4"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/luau) = %{version}
Requires:       crate(mlua-sys-0.10/luau-vector4) >= 0.10.0
Provides:       crate(%{pkgname}/luau-vector4) = %{version}

%description -n %{name}+luau-vector4
This metapackage enables feature "luau-vector4" for the Rust mlua crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+macros
Summary:        High level bindings to Lua 5.5/5.4/5.3/5.2/5.1 (including LuaJIT) and Luau with async/await features and support of writing native Lua modules in Rust - feature "macros"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mlua-derive-0.11/macros) >= 0.11.0
Provides:       crate(%{pkgname}/macros) = %{version}

%description -n %{name}+macros
This metapackage enables feature "macros" for the Rust mlua crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mlua-derive
Summary:        High level bindings to Lua 5.5/5.4/5.3/5.2/5.1 (including LuaJIT) and Luau with async/await features and support of writing native Lua modules in Rust - feature "mlua_derive"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mlua-derive-0.11/default) >= 0.11.0
Provides:       crate(%{pkgname}/mlua-derive) = %{version}

%description -n %{name}+mlua-derive
This metapackage enables feature "mlua_derive" for the Rust mlua crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+module
Summary:        High level bindings to Lua 5.5/5.4/5.3/5.2/5.1 (including LuaJIT) and Luau with async/await features and support of writing native Lua modules in Rust - feature "module"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/mlua-derive) = %{version}
Requires:       crate(mlua-sys-0.10/module) >= 0.10.0
Provides:       crate(%{pkgname}/module) = %{version}

%description -n %{name}+module
This metapackage enables feature "module" for the Rust mlua crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        High level bindings to Lua 5.5/5.4/5.3/5.2/5.1 (including LuaJIT) and Luau with async/await features and support of writing native Lua modules in Rust - feature "serde" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bstr-1/serde) >= 1.0.0
Requires:       crate(bstr-1/std) >= 1.0.0
Requires:       crate(erased-serde-0.4/default) >= 0.4.0
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-value-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/serde) = %{version}
Provides:       crate(%{pkgname}/serialize) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust mlua crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "serialize" feature.

%package     -n %{name}+userdata-wrappers
Summary:        High level bindings to Lua 5.5/5.4/5.3/5.2/5.1 (including LuaJIT) and Luau with async/await features and support of writing native Lua modules in Rust - feature "userdata-wrappers"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(parking-lot-0.12/arc-lock) >= 0.12.0
Requires:       crate(parking-lot-0.12/send-guard) >= 0.12.0
Provides:       crate(%{pkgname}/userdata-wrappers) = %{version}

%description -n %{name}+userdata-wrappers
This metapackage enables feature "userdata-wrappers" for the Rust mlua crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vendored
Summary:        High level bindings to Lua 5.5/5.4/5.3/5.2/5.1 (including LuaJIT) and Luau with async/await features and support of writing native Lua modules in Rust - feature "vendored"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mlua-sys-0.10/vendored) >= 0.10.0
Provides:       crate(%{pkgname}/vendored) = %{version}

%description -n %{name}+vendored
This metapackage enables feature "vendored" for the Rust mlua crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
