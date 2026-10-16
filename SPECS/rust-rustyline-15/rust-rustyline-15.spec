# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustyline
%global full_version 15.0.0
%global pkgname rustyline-15

Name:           rust-rustyline-15
Version:        15.0.0
Release:        %autorelease
Summary:        Rust crate "rustyline"
License:        MIT
URL:            https://github.com/kkawakam/rustyline
#!RemoteAsset:  sha256:2ee1e066dc922e513bda599c6ccb5f3bb2b0ea5870a579448f2622993f0a9a2f
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2/default) >= 2.6.0
Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(clipboard-win-5/default) >= 5.0.0
Requires:       crate(libc-0.2/default) >= 0.2.155
Requires:       crate(log-0.4/default) >= 0.4.22
Requires:       crate(memchr-2/default) >= 2.7.0
Requires:       crate(nix-0.29/fs) >= 0.29.0
Requires:       crate(nix-0.29/ioctl) >= 0.29.0
Requires:       crate(nix-0.29/poll) >= 0.29.0
Requires:       crate(nix-0.29/signal) >= 0.29.0
Requires:       crate(nix-0.29/term) >= 0.29.0
Requires:       crate(unicode-segmentation-1/default) >= 1.0.0
Requires:       crate(unicode-width-0.2/default) >= 0.2.0
Requires:       crate(utf8parse-0.2/default) >= 0.2.0
Requires:       crate(windows-sys-0.59/default) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-foundation) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-security) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-console) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-system-threading) >= 0.59.0
Requires:       crate(windows-sys-0.59/win32-ui-input-keyboardandmouse) >= 0.59.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "rustyline"

%package     -n %{name}+buffer-redux
Summary:        Readline implementation based on Antirez's Linenoise - feature "buffer-redux"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(buffer-redux-1) >= 1.0.0
Provides:       crate(%{pkgname}/buffer-redux) = %{version}

%description -n %{name}+buffer-redux
This metapackage enables feature "buffer-redux" for the Rust rustyline crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Readline implementation based on Antirez's Linenoise - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/custom-bindings) = %{version}
Requires:       crate(%{pkgname}/with-dirs) = %{version}
Requires:       crate(%{pkgname}/with-file-history) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust rustyline crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fd-lock
Summary:        Readline implementation based on Antirez's Linenoise - feature "fd-lock" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(fd-lock-4/default) >= 4.0.0
Provides:       crate(%{pkgname}/fd-lock) = %{version}
Provides:       crate(%{pkgname}/with-file-history) = %{version}

%description -n %{name}+fd-lock
This metapackage enables feature "fd-lock" for the Rust rustyline crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "with-file-history" feature.

%package     -n %{name}+home
Summary:        Readline implementation based on Antirez's Linenoise - feature "home" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(home-0.5/default) >= 0.5.4
Provides:       crate(%{pkgname}/home) = %{version}
Provides:       crate(%{pkgname}/with-dirs) = %{version}

%description -n %{name}+home
This metapackage enables feature "home" for the Rust rustyline crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "with-dirs" feature.

%package     -n %{name}+radix-trie
Summary:        Readline implementation based on Antirez's Linenoise - feature "radix_trie" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(radix-trie-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/custom-bindings) = %{version}
Provides:       crate(%{pkgname}/radix-trie) = %{version}

%description -n %{name}+radix-trie
This metapackage enables feature "radix_trie" for the Rust rustyline crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "custom-bindings" feature.

%package     -n %{name}+regex
Summary:        Readline implementation based on Antirez's Linenoise - feature "regex" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-1/default) >= 1.10.0
Provides:       crate(%{pkgname}/case-insensitive-history-search) = %{version}
Provides:       crate(%{pkgname}/regex) = %{version}

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust rustyline crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "case_insensitive_history_search" feature.

%package     -n %{name}+rusqlite
Summary:        Readline implementation based on Antirez's Linenoise - feature "rusqlite" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rusqlite-0.32/backup) >= 0.32.0
Requires:       crate(rusqlite-0.32/bundled) >= 0.32.0
Provides:       crate(%{pkgname}/rusqlite) = %{version}
Provides:       crate(%{pkgname}/with-sqlite-history) = %{version}

%description -n %{name}+rusqlite
This metapackage enables feature "rusqlite" for the Rust rustyline crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "with-sqlite-history" feature.

%package     -n %{name}+rustyline-derive
Summary:        Readline implementation based on Antirez's Linenoise - feature "rustyline-derive" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rustyline-derive-0.11/default) >= 0.11.0
Provides:       crate(%{pkgname}/derive) = %{version}
Provides:       crate(%{pkgname}/rustyline-derive) = %{version}

%description -n %{name}+rustyline-derive
This metapackage enables feature "rustyline-derive" for the Rust rustyline crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "derive" feature.

%package     -n %{name}+signal-hook
Summary:        Readline implementation based on Antirez's Linenoise - feature "signal-hook"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(signal-hook-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/signal-hook) = %{version}

%description -n %{name}+signal-hook
This metapackage enables feature "signal-hook" for the Rust rustyline crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+skim
Summary:        Readline implementation based on Antirez's Linenoise - feature "skim" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(skim-0.10) >= 0.10.0
Provides:       crate(%{pkgname}/skim) = %{version}
Provides:       crate(%{pkgname}/with-fuzzy) = %{version}

%description -n %{name}+skim
This metapackage enables feature "skim" for the Rust rustyline crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "with-fuzzy" feature.

%package     -n %{name}+termios
Summary:        Readline implementation based on Antirez's Linenoise - feature "termios"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(termios-0.3/default) >= 0.3.3
Provides:       crate(%{pkgname}/termios) = %{version}

%description -n %{name}+termios
This metapackage enables feature "termios" for the Rust rustyline crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
