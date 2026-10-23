# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go-git
%define go_import_path  github.com/go-git/go-git/v6
# These cases contact GitHub/GitLab; OBS reports DNS connection refused or
# Service Unavailable, including TestFetchByHashThenResolveRevision.
# TestConfigScoped additionally assumes /etc/gitconfig
# contains a user email, but OBS has none. Keep local transport tests enabled.
%global go_test_flags_default -v -skip '^TestFetchByHashThenResolveRevision$|^Example(Plain)?Clone$|^TestWorktreeSuite$/^TestCheckout(RelativePath)?SubmoduleInitialized$|^TestRemoteSuite$/^Test(FetchExactSHA1|FetchOfMissingObjects|List|ListPeeling)$|^TestRepositorySuite$/^Test(CloneMirror|CloneWithFilter|FetchWithFiltersReal|ConfigScoped)$|^TestUploadPackSuite$/^TestAdvertisedReferences(Context|RedirectPath|RedirectSchema)$|^TestProxySuite$/^TestAdvertisedReferencesHTTPS$'

Name:           go-github-go-git-go-git-v6
Version:        6.0.0~beta1
Release:        %autorelease
Summary:        Pure Go Git implementation
License:        Apache-2.0
URL:            https://github.com/go-git/go-git
#!RemoteAsset:  sha256:37eb6ce5cae3a284f47f2f6cc34e9eacaf8f055dba1dd3afe939978b08974a3e
Source0:        https://github.com/go-git/go-git/archive/v6.0.0-beta.1.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-6.0.0-beta.1

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
BuildRequires:  go(github.com/go-git/go-git-fixtures/v6)
BuildRequires:  go(github.com/kevinburke/ssh_config)
BuildRequires:  go(github.com/pjbgf/sha1cd)
BuildRequires:  go(github.com/sergi/go-diff)
BuildRequires:  go(github.com/stretchr/testify)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/sync)
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
Requires:       go(github.com/go-git/go-git-fixtures/v6)
Requires:       go(github.com/kevinburke/ssh_config)
Requires:       go(github.com/pjbgf/sha1cd)
Requires:       go(github.com/sergi/go-diff)
Requires:       go(github.com/stretchr/testify)
Requires:       go(golang.org/x/crypto)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/sync)
Requires:       go(golang.org/x/sys)

%description
Go implementation of Git repository operations, including objects,
references, storage and network transports.

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
