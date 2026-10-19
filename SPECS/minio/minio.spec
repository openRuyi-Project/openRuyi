# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Julian Zhu <julian.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Kimmy <yucheng.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           minio
%define go_import_path  github.com/minio/minio
# These endpoint tests resolve example.org/com/net. Offline OBS reports
# "lookup example.org on [::1]:53: ... connection refused".
%global go_test_flags_default -v -skip '^(TestNewEndpoint|TestCreateEndpoints|TestGetLocalPeer|TestGetRemotePeers|TestCheckLocalServerAddr)$'

Name:           minio
Version:        2025.10.15T17.29.55Z
Release:        %autorelease
Summary:        High-performance S3-compatible object storage server
License:        AGPL-3.0-or-later
URL:            https://github.com/minio/minio
#!RemoteAsset:  sha256:be6d0bd3696c3a13a35f02d3a0280b64319c67918b4501c5c3d87f96d000085c
Source0:        https://github.com/minio/minio/archive/RELEASE.2025-10-15T17-29-55Z.tar.gz#/minio-RELEASE.2025-10-15T17-29-55Z.tar.gz
BuildSystem:    golang

# minio/sio 0.5 renamed its AES-GCM identifier without changing the wire value.
Patch2000:      2000-use-renamed-sio-aes-gcm-identifier.patch
# Go printf analysis rejects quoting the grid test response structure with %q.
Patch2001:      2001-fix-grid-response-test-format.patch

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(aead.dev/mtls)
BuildRequires:  go(cloud.google.com/go/storage)
BuildRequires:  go(github.com/Azure/azure-sdk-for-go)
BuildRequires:  go(github.com/IBM/sarama)
BuildRequires:  go(github.com/alecthomas/participle)
BuildRequires:  go(github.com/beevik/ntp)
BuildRequires:  go(github.com/buger/jsonparser)
BuildRequires:  go(github.com/cespare/xxhash/v2)
BuildRequires:  go(github.com/cheggaaa/pb)
BuildRequires:  go(github.com/coreos/go-oidc/v3)
BuildRequires:  go(github.com/coreos/go-systemd/v22)
BuildRequires:  go(github.com/cosnicolaou/pbzip2)
BuildRequires:  go(github.com/dchest/siphash)
BuildRequires:  go(github.com/dustin/go-humanize)
BuildRequires:  go(github.com/eclipse/paho.mqtt.golang)
BuildRequires:  go(github.com/elastic/go-elasticsearch/v7)
BuildRequires:  go(github.com/fatih/color)
BuildRequires:  go(github.com/felixge/fgprof)
BuildRequires:  go(github.com/fraugster/parquet-go)
BuildRequires:  go(github.com/go-ldap/ldap/v3)
BuildRequires:  go(github.com/go-openapi/loads)
BuildRequires:  go(github.com/go-sql-driver/mysql)
BuildRequires:  go(github.com/gobwas/ws)
BuildRequires:  go(github.com/golang-jwt/jwt/v4)
BuildRequires:  go(github.com/gomodule/redigo)
BuildRequires:  go(github.com/google/uuid)
BuildRequires:  go(github.com/inconshreveable/mousetrap)
BuildRequires:  go(github.com/json-iterator/go)
BuildRequires:  go(github.com/klauspost/compress)
BuildRequires:  go(github.com/klauspost/cpuid/v2)
BuildRequires:  go(github.com/klauspost/filepathx)
BuildRequires:  go(github.com/klauspost/pgzip)
BuildRequires:  go(github.com/klauspost/readahead)
BuildRequires:  go(github.com/klauspost/reedsolomon)
BuildRequires:  go(github.com/lib/pq)
BuildRequires:  go(github.com/lithammer/shortuuid/v4)
BuildRequires:  go(github.com/miekg/dns)
BuildRequires:  go(github.com/minio/cli)
BuildRequires:  go(github.com/minio/console)
BuildRequires:  go(github.com/minio/csvparser)
BuildRequires:  go(github.com/minio/dnscache)
BuildRequires:  go(github.com/minio/dperf)
BuildRequires:  go(github.com/minio/highwayhash)
BuildRequires:  go(github.com/minio/kms-go)
BuildRequires:  go(github.com/minio/madmin-go/v3)
BuildRequires:  go(github.com/minio/minio-go/v7)
BuildRequires:  go(github.com/minio/mux)
BuildRequires:  go(github.com/minio/pkg/v3)
BuildRequires:  go(github.com/minio/selfupdate)
BuildRequires:  go(github.com/minio/simdjson-go)
BuildRequires:  go(github.com/minio/sio)
BuildRequires:  go(github.com/minio/xxml)
BuildRequires:  go(github.com/minio/zipindex)
BuildRequires:  go(github.com/mitchellh/go-homedir)
BuildRequires:  go(github.com/nats-io/nats-server/v2)
BuildRequires:  go(github.com/nats-io/nats.go)
BuildRequires:  go(github.com/nats-io/stan.go)
BuildRequires:  go(github.com/ncw/directio)
BuildRequires:  go(github.com/nsqio/go-nsq)
BuildRequires:  go(github.com/philhofer/fwd)
BuildRequires:  go(github.com/pierrec/lz4/v4)
BuildRequires:  go(github.com/pkg/errors)
BuildRequires:  go(github.com/pkg/sftp)
BuildRequires:  go(github.com/pkg/xattr)
BuildRequires:  go(github.com/prometheus/client_golang)
BuildRequires:  go(github.com/prometheus/client_model)
BuildRequires:  go(github.com/prometheus/common)
BuildRequires:  go(github.com/prometheus/procfs)
BuildRequires:  go(github.com/puzpuzpuz/xsync/v3)
BuildRequires:  go(github.com/rabbitmq/amqp091-go)
BuildRequires:  go(github.com/rcrowley/go-metrics)
BuildRequires:  go(github.com/rs/cors)
BuildRequires:  go(github.com/secure-io/sio-go)
BuildRequires:  go(github.com/shirou/gopsutil/v3)
BuildRequires:  go(github.com/tinylib/msgp)
BuildRequires:  go(github.com/valyala/bytebufferpool)
BuildRequires:  go(github.com/xdg/scram)
BuildRequires:  go(github.com/zeebo/xxh3)
BuildRequires:  go(go.etcd.io/etcd/api/v3)
BuildRequires:  go(go.etcd.io/etcd/client/v3)
BuildRequires:  go(go.uber.org/atomic)
BuildRequires:  go(go.uber.org/zap)
BuildRequires:  go(goftp.io/server/v2)
BuildRequires:  go(golang.org/x/crypto)
BuildRequires:  go(golang.org/x/oauth2)
BuildRequires:  go(golang.org/x/sync)
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/term)
BuildRequires:  go(golang.org/x/time)
BuildRequires:  go(google.golang.org/api/googleapi)
BuildRequires:  go(google.golang.org/api/iterator)
BuildRequires:  go(google.golang.org/api/option)
BuildRequires:  go(gopkg.in/yaml.v2)
BuildRequires:  go(gopkg.in/yaml.v3)

%description
MinIO is an S3-compatible object storage server for AI, analytics and other
data-intensive workloads. It builds against distribution-provided Go libraries.

%build
%go_common
# The canonical import comment requires building inside the GOPATH workspace.
minio_build_dir="$PWD"
cd %{_builddir}/go/src/%{go_import_path}
go build -v -buildmode=pie -trimpath -o "$minio_build_dir/%{_name}" .

%files
%doc README.md
%license LICENSE
%{_bindir}/%{_name}

%changelog
%autochangelog
