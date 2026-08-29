# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           go4
%define go_import_path  go4.org
%define commit_id       a5071408f32fb3d4c99310ecae0f7fada8a8a991

Name:           go-go4
Version:        0+git20260718.a507140
Release:        %autorelease
Summary:        Collection of packages for Go programmers
License:        Apache-2.0
URL:            https://github.com/go4org/go4
#!RemoteAsset:  sha256:5890273a558115e56e54e58f9444d37868f80aae1cd8a5169a4735763052f2d5
Source0:        https://github.com/go4org/go4/archive/%{commit_id}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n %{_name}-%{commit_id}

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(cloud.google.com/go/compute/metadata)
BuildRequires:  go(cloud.google.com/go/storage)
BuildRequires:  go(github.com/rwcarlsen/goexif)
BuildRequires:  go(golang.org/x/net)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(google.golang.org/api)

Provides:       go(go4.org) = %{version}
Provides:       go(go4.org/bytereplacer) = %{version}
Provides:       go(go4.org/cloud/cloudlaunch) = %{version}
Provides:       go(go4.org/cloud/google/gceutil) = %{version}
Provides:       go(go4.org/cloud/google/gcsutil) = %{version}
Provides:       go(go4.org/ctxutil) = %{version}
Provides:       go(go4.org/errorutil) = %{version}
Provides:       go(go4.org/fault) = %{version}
Provides:       go(go4.org/jsonconfig) = %{version}
Provides:       go(go4.org/legal) = %{version}
Provides:       go(go4.org/lock) = %{version}
Provides:       go(go4.org/media/heif) = %{version}
Provides:       go(go4.org/media/heif/bmff) = %{version}
Provides:       go(go4.org/must) = %{version}
Provides:       go(go4.org/net/throttle) = %{version}
Provides:       go(go4.org/oauthutil) = %{version}
Provides:       go(go4.org/osutil) = %{version}
Provides:       go(go4.org/readerutil) = %{version}
Provides:       go(go4.org/readerutil/singlereader) = %{version}
Provides:       go(go4.org/reflectutil) = %{version}
Provides:       go(go4.org/rollsum) = %{version}
Provides:       go(go4.org/sort) = %{version}
Provides:       go(go4.org/strutil) = %{version}
Provides:       go(go4.org/syncutil) = %{version}
Provides:       go(go4.org/syncutil/singleflight) = %{version}
Provides:       go(go4.org/syncutil/syncdebug) = %{version}
Provides:       go(go4.org/testing/functest) = %{version}
Provides:       go(go4.org/types) = %{version}
Provides:       go(go4.org/wkfs) = %{version}
Provides:       go(go4.org/wkfs/gcs) = %{version}
Provides:       go(go4.org/writerutil) = %{version}
Provides:       go(go4.org/xdgdir) = %{version}
Provides:       go(go4.org/ziputil) = %{version}

Requires:       go(cloud.google.com/go/compute/metadata)
Requires:       go(cloud.google.com/go/storage)
Requires:       go(github.com/rwcarlsen/goexif)
Requires:       go(golang.org/x/net)
Requires:       go(golang.org/x/oauth2)
Requires:       go(golang.org/x/sys)
Requires:       go(google.golang.org/api)

%description
go4.org is a collection of packages for Go programmers.
They started out living in Perkeep's repo and elsewhere
but they have nothing to do with Perkeep, so we're moving
them here.

%check -p
# Keep panic(nil) behavior consistent with Go 1.21+ during GOPATH-mode tests. - Jvle
export GODEBUG="${GODEBUG:+${GODEBUG},}panicnil=0"

%files
%doc README.md
%license LICENSE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog
