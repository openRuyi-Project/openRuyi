# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global _name           go-git
%define go_import_path  github.com/go-git/go-git/v6
%global commit_id       e6a3f881772f25a76178463b6d71e610ea5a8180
# These cases contact GitHub/GitLab; OBS reports DNS connection refused or
# Service Unavailable. TestConfigScoped additionally assumes /etc/gitconfig
# contains a user email, but OBS has none. Keep local transport tests enabled.
%global go_test_flags_default -v -skip '^Example(Plain)?Clone$|^TestWorktreeSuite$/^TestCheckout(RelativePath)?SubmoduleInitialized$|^TestRemoteSuite$/^Test(FetchExactSHA1|FetchOfMissingObjects|List|ListPeeling)$|^TestRepositorySuite$/^Test(CloneMirror|CloneWithFilter|FetchWithFiltersReal|ConfigScoped)$|^TestUploadPackSuite$/^TestAdvertisedReferences(Context|RedirectPath|RedirectSchema)$|^TestProxySuite$/^TestAdvertisedReferencesHTTPS$'

Name:           go-github-go-git-go-git-v6
Version:        5.12.0+git20261023.e6a3f88
Release:        %autorelease
Summary:        Pure Go Git implementation
License:        Apache-2.0
URL:            https://github.com/go-git/go-git
#!RemoteAsset:  sha256:68fb546ed3fb6f4a6d50e6bca65d11b9e639c5a1ead007b623842ab0e5c9157b
Source0:        https://github.com/go-git/go-git/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

# Backport the Go 1.27 compression expectation fix to this v6 snapshot.
# https://github.com/go-git/go-git/commit/4ae786a01dfb96289854ddc6460981531a6fe53c
Patch1000:      1000-tests-derive-zlib-expectations.patch
# Reserve the packet header so large sideband writes work with Go 1.27.
# https://github.com/go-git/go-git/commit/0551cb44e98df61aad9054d24220aa1eb9d5508a
Patch1001:      1001-sideband-reserve-pkt-line-header.patch
# Use IPv4 for the IPv4-only test daemon and an explicit fixture tag identity.
Patch2000:      2000-make-test-environment-explicit.patch

# OBS has no external DNS; honor upstream's short-mode network exclusions.
BuildOption(check):  -short

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(github.com/ProtonMail/go-crypto)
BuildRequires:  go(github.com/armon/go-socks5)
BuildRequires:  go(github.com/emirpasic/gods)
BuildRequires:  go(github.com/gliderlabs/ssh)
BuildRequires:  go(github.com/go-git/gcfg/v2)
BuildRequires:  go(github.com/go-git/go-billy/v6)
BuildRequires:  go(github.com/go-git/go-git-fixtures/v5)
BuildRequires:  go(github.com/golang/groupcache)
BuildRequires:  go(github.com/kevinburke/ssh_config)
BuildRequires:  go(github.com/pjbgf/sha1cd)
BuildRequires:  go(github.com/sergi/go-diff)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/text)
# Tests execute Git and load Europe/Berlin through time.LoadLocation.
BuildRequires:  git
BuildRequires:  git-daemon
BuildRequires:  tzdata

Provides:       go(github.com/go-git/go-git/v6) = %{version}

Requires:       go(github.com/ProtonMail/go-crypto)
Requires:       go(github.com/emirpasic/gods)
Requires:       go(github.com/go-git/gcfg/v2)
Requires:       go(github.com/go-git/go-billy/v6)
Requires:       go(github.com/go-git/go-git-fixtures/v5)
Requires:       go(github.com/golang/groupcache)
Requires:       go(github.com/kevinburke/ssh_config)
Requires:       go(github.com/pjbgf/sha1cd)
Requires:       go(github.com/sergi/go-diff)
Requires:       go(github.com/stretchr/testify)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sys)

%description
Go implementation of Git repository operations, including objects,
references, storage and network transports.

%prep
%autosetup -n %{_name}-%{commit_id} -p1

%check -p
# Commit tests obtain their default author from the global Git configuration.
export XDG_CONFIG_HOME=%{_builddir}/git-test-config
export GIT_AUTHOR_NAME="Go Git Tests"
export GIT_AUTHOR_EMAIL=tests@example.invalid
export GIT_COMMITTER_NAME="$GIT_AUTHOR_NAME"
export GIT_COMMITTER_EMAIL="$GIT_AUTHOR_EMAIL"
export SSH_KNOWN_HOSTS=%{_builddir}/git-test-known-hosts
touch "$SSH_KNOWN_HOSTS"
mkdir -p "$XDG_CONFIG_HOME/git"
cat > "$XDG_CONFIG_HOME/git/config" <<'EOF'
[user]
    name = Go Git Tests
    email = tests@example.invalid
EOF

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
