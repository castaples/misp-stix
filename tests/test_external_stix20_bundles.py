#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import deepcopy
from stix2.parsing import dict_to_stix2


_ARTIFACT_OBJECTS = [
    {
        "type": "observed-data",
        "id": "observed-data--3cd23a7b-a099-49df-b397-189018311d4e",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa952",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-11-25T16:22:00.000Z",
        "first_observed": "2020-10-25T16:22:00Z",
        "last_observed": "2020-11-25T16:22:00Z",
        "number_observed": 1,
        "objects": {
            "0": {
                "type": "artifact",
                "mime_type": "application/zip",
                "payload_bin": "UEsDBAoACQAAAKBINlgCq9FEEAAAAAQAAAADABwAb3VpVVQJAAOrIa5lrSGuZXV4CwABBPUBAAAEFAAAAOLQGBmrTcdmURq/qqA1qFFQSwcIAqvRRBAAAAAEAAAAUEsBAh4DCgAJAAAAoEg2WAKr0UQQAAAABAAAAAMAGAAAAAAAAQAAAKSBAAAAAG91aVVUBQADqyGuZXV4CwABBPUBAAAEFAAAAFBLBQYAAAAAAQABAEkAAABdAAAAAAA=",
                "hashes": {
                    "MD5": "bc590af5f7b16b890860248dc0d4c68f",
                    "SHA-1": "003d59659a3e28781aaf03da1ac1cb0e326ed65e",
                    "SHA-256": "2dd39c08867f34010fd9ea1833aa549a02da16950dda4a8ef922113a9eccd963"
                },
                "decryption_key": "infected",
            },
            "1": {
                "type": "artifact",
                "url": "https://files.pythonhosted.org/packages/1a/62/29f55ef42483c30281fab9d3282ac467f215501826f3251678d8ec2da2e1/misp_stix-2.4.183.tar.gz",
                "hashes": {
                    "MD5": "b3982699c1b9a25346cc8498f483b150",
                    "SHA-256": "836f395a4f86e9d1b2f528756c248e76665c02c5d0fc89f9b26136db5ac7f7ae"
                }
            }
        }
    },
    {
        "type": "observed-data",
        "id": "observed-data--3451329f-2525-4bcb-9659-7bd0e6f1eb0d",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa952",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "first_observed": "2020-10-25T16:22:00Z",
        "last_observed": "2020-10-25T16:22:00Z",
        "number_observed": 1,
        "objects": {
            "0": {
                "type": "artifact",
                "mime_type": "application/zip",
                "payload_bin": "UEsDBAoACQAAANVUNlgGfJ2iEAAAAAQAAAADABwAbm9uVVQJAAOhN65lozeuZXV4CwABBPUBAAAEFAAAAE7nhRTz5ElBwvqrXUHYVMlQSwcIBnydohAAAAAEAAAAUEsBAh4DCgAJAAAA1VQ2WAZ8naIQAAAABAAAAAMAGAAAAAAAAQAAAKSBAAAAAG5vblVUBQADoTeuZXV4CwABBPUBAAAEFAAAAFBLBQYAAAAAAQABAEkAAABdAAAAAAA=",
                "hashes": {
                    "MD5": "5bfd0814254d0ff993a83560cb740042",
                    "SHA-1": "5ec1405887e5a74bf2cb97a8d64481194dc13fdc",
                    "SHA-256": "367e474683cb1f61aae1f963aa9a17446afb5f71a8a03dae7203ac84765a5efa"
                },
                "decryption_key": "clear",
            }
        }
    }
]
_AS_OBJECTS = [
    {
        "type": "observed-data",
        "id": "observed-data--3cd23a7b-a099-49df-b397-189018311d4e",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa952",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-11-25T16:22:00.000Z",
        "first_observed": "2020-10-25T16:22:00Z",
        "last_observed": "2020-11-25T16:22:00Z",
        "number_observed": 1,
        "objects": {
            "0": {
                "type": "autonomous-system",
                "number": 666,
                "name": "Satan autonomous system"
            },
            "1": {
                "type": "autonomous-system",
                "number": 1234
            }
        }
    },
    {
        "type": "observed-data",
        "id": "observed-data--3451329f-2525-4bcb-9659-7bd0e6f1eb0d",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa952",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "first_observed": "2020-10-25T16:22:00Z",
        "last_observed": "2020-10-25T16:22:00Z",
        "number_observed": 1,
        "objects": {
            "0": {
                "type": "autonomous-system",
                "number": 197869,
                "name": "CIRCL"
            }
        }
    },
    {
        "type": "observed-data",
        "id": "observed-data--1bf81a4f-0e70-4a34-944b-7e46f67ff7a7",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa952",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-11-25T16:22:00.000Z",
        "first_observed": "2020-10-25T16:22:00Z",
        "last_observed": "2020-11-25T16:22:00Z",
        "number_observed": 1,
        "objects": {
            "0": {
                "type": "autonomous-system",
                "number": 50588
            }
        }
    }
]
_ATTACK_PATTERN_OBJECTS = [
    {
        "type": "attack-pattern",
        "id": "attack-pattern--19da6e1c-69a8-4c2f-886d-d620d09d3b5a",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa951",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "external_references": [
            {
                "source_name": "capec",
                "description": "spear phishing",
                "external_id": "CAPEC-163"
            }
        ],
        "name": "Spear Phishing Attack Pattern used by admin@338",
        "description": "The preferred attack vector used by admin@338 is spear-phishing emails. Using content that is relevant to the target, these emails are designed to entice the target to open an attachment that contains the malicious PIVY server code.",
        "kill_chain_phases": [
            {
                "kill_chain_name": "mandiant-attack-lifecycle-model",
                "phase_name": "initial-compromise"
            }
        ]
    },
    {
        "type": "attack-pattern",
        "id": "attack-pattern--ea2c747d-4aa3-4573-8853-37b7159bc180",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa951",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "name": "Strategic Web Compromise Attack Pattern used by th3bug",
        "description": "Attacks attributed to th3bug use a strategic Web compromise to infect targets. This approach is more indiscriminate, which probably accounts for the more disparate range of targets.",
        "kill_chain_phases": [
            {
                "kill_chain_name": "mandiant-attack-lifecycle-model",
                "phase_name": "initial-compromise"
            }
        ]
    }
]
_CAMPAIGN_OBJECTS = [
    {
        "type": "campaign",
        "id": "campaign--752c225d-d6f6-4456-9130-d9580fd4007b",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa951",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "name": "admin@338",
        "description": "Active since 2008, this campaign mostly targets the financial services industry, though we have also seen activity in the telecom, government, and defense sectors.",
        "first_seen": "2020-10-25T16:22:00.000Z"
    },
    {
        "type": "campaign",
        "id": "campaign--d02a1560-ff69-49f4-ac34-919b8aa4b91e",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa951",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "name": "th3bug",
        "description": "This ongoing campaign targets a number of industries but appears to prefer targets in higher education and the healthcare sectors.",
        "first_seen": "2020-10-25T16:22:00.000Z"
    }
]
_COURSE_OF_ACTION_OBJECTS = [
    {
        "type": "course-of-action",
        "id": "course-of-action--70b3d5f6-374b-4488-8688-729b6eedac5b",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa951",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "name": "Analyze with FireEye Calamine Toolset",
        "description": "Calamine is a set of free tools to help organizations detect and examine Poison Ivy infections on their systems. The package includes these components: PIVY callback-decoding tool (ChopShop Module) and PIVY memory-decoding tool (PIVY PyCommand Script).",
        "external_references": [
            {
                "source_name": "Calamine ChopShop Module",
                "description": "The FireEye Poison Ivy decoder checks the beginning of each TCP session for possible PIVY challengeresponse sequences. If found, the module will try to validate the response using one or more passwords supplied as arguments.",
                "url": "https://github.com/fireeye/chopshop"
            },
            {
                "source_name": "Calamine PyCommand Script",
                "description": "Helps locate the PIVY password.",
                "url": "https://github.com/fireeye/pycommands"
            }
        ]
    },
    {
        "type": "course-of-action",
        "id": "course-of-action--e84ac8d4-dd81-4b04-81b6-d72137c21c84",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa951",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "name": "Exploitation for Client Execution Mitigation",
        "description": "Browser sandboxes can be used to mitigate some of the impact of exploitation, but sandbox escapes may still exist",
        "external_references": [
            {
                "source_name": "MITRE",
                "url": "https://attack.mitre.org/mitigations/T1203"
            },
            {
                "source_name": "MITRE ATT&CK",
                "external_id": "T1203"
            }
        ]
    }
]
_DIRECTORY_OBJECTS = [
    {
        "type": "observed-data",
        "id": "observed-data--5e384ae7-672c-4250-9cda-3b4da964451a",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa951",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "first_observed": "2020-10-25T16:22:00Z",
        "last_observed": "2020-10-25T16:22:00Z",
        "number_observed": 1,
        "objects": {
            "0": {
                "type": "directory",
                "path": "/var/www/MISP/app/files/scripts/misp-stix",
                "path_enc": "ISO-8859-1",
                "created": "2021-07-21T11:44:56Z",
                "modified": "2023-12-12T11:24:30Z",
                "accessed": "2023-12-12T11:24:30Z"
            }
        }
    },
    {
        "type": "observed-data",
        "id": "observed-data--5ac47782-e1b8-40b6-96b4-02510a00020f",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa951",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-11-25T16:22:00.000Z",
        "first_observed": "2020-10-25T16:22:00Z",
        "last_observed": "2020-11-25T16:22:00Z",
        "number_observed": 1,
        "objects": {
            "0": {
                "type": "directory",
                "path": "/var/www/MISP/app/files/scripts/",
                "path_enc": "ISO-8859-6-I",
                "created": "2014-07-25T10:47:08Z",
                "modified": "2023-12-12T11:34:05Z",
                "accessed": "2023-12-12T11:34:05Z",
                "contains_refs": [
                    "1"
                ]
            },
            "1": {
                "type": "directory",
                "path": "/var/www/MISP/app/files/scripts/misp-stix",
                "path_enc": "ISO-8859-1",
                "created": "2021-07-21T11:44:56Z",
                "modified": "2023-12-12T11:24:30Z",
                "accessed": "2023-12-12T11:24:30Z"
            }
        }
    }
]
_DOMAIN_ATTRIBUTES = [
    {
        "type": "observed-data",
        "id": "observed-data--3cd23a7b-a099-49df-b397-189018311d4e",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa952",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-11-25T16:22:00.000Z",
        "first_observed": "2020-10-25T16:22:00Z",
        "last_observed": "2020-11-25T16:22:00Z",
        "number_observed": 1,
        "objects": {
            "0": {
                "type": "domain-name",
                "value": "circl.lu"
            },
            "1": {
                "type": "domain-name",
                "value": "lhc.lu"
            }
        }
    },
    {
        "type": "observed-data",
        "id": "observed-data--3451329f-2525-4bcb-9659-7bd0e6f1eb0d",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa952",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "first_observed": "2020-10-25T16:22:00Z",
        "last_observed": "2020-10-25T16:22:00Z",
        "number_observed": 1,
        "objects": {
            "0": {
                "type": "domain-name",
                "value": "misp-project.org"
            }
        }
    }
]
_EMAIL_ADDRESS_ATTRIBUTES = [
    {
        "type": "observed-data",
        "id": "observed-data--3cd23a7b-a099-49df-b397-189018311d4e",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa952",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-11-25T16:22:00.000Z",
        "first_observed": "2020-10-25T16:22:00Z",
        "last_observed": "2020-11-25T16:22:00Z",
        "number_observed": 1,
        "objects": {
            "0": {
                "type": "email-addr",
                "value": "john.doe@gmail.com",
                "display_name": "John Doe"
            },
            "1": {
                "type": "email-addr",
                "value": "john@doe.org"
            }
        }
    },
    {
        "type": "observed-data",
        "id": "observed-data--3451329f-2525-4bcb-9659-7bd0e6f1eb0d",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa952",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "first_observed": "2020-10-25T16:22:00Z",
        "last_observed": "2020-10-25T16:22:00Z",
        "number_observed": 1,
        "objects": {
            "0": {
                "type": "email-addr",
                "value": "donald.duck@disney.com",
                "display_name": "Donald Duck"
            }
        }
    },
    {
        "type": "observed-data",
        "id": "observed-data--1bf81a4f-0e70-4a34-944b-7e46f67ff7a7",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa952",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-11-25T16:22:00.000Z",
        "first_observed": "2020-10-25T16:22:00Z",
        "last_observed": "2020-11-25T16:22:00Z",
        "number_observed": 1,
        "objects": {
            "0": {
                "type": "email-addr",
                "value": "donald.duck@gmail.com"
            }
        }
    }
]
_INTRUSION_SET_OBJECTS = [
    {
        "type": "intrusion-set",
        "id": "intrusion-set--da1065ce-972c-4605-8755-9cd1074e3b5a",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa951",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "name": "APT1",
        "description": "APT1 is a single organization of operators that has conducted a cyber espionage campaign against a broad range of victims since at least 2006.",
        "first_seen": "2020-10-25T16:22:00.000Z",
        "resource_level": "government",
        "primary_motivation": "organizational-gain",
        "aliases": [
            "Comment Crew",
            "Comment Group",
            "Shady Rat"
        ]
    },
    {
        "type": "intrusion-set",
        "id": "intrusion-set--10df003c-7831-41e7-bdb9-971cdd1218df",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa951",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "name": "Lazarus Group - G0032",
        "first_seen": "2020-10-25T16:22:00.000Z",
        "resource_level": "government",
        "primary_motivation": "organizational-gain",
        "aliases": [
            "Lazarus Group",
            "HIDDEN COBRA",
            "Guardians of Peace",
            "ZINC",
            "NICKEL ACADEMY"
        ]
    }
]
_IP_ADDRESS_ATTRIBUTES = [
    {
        "type": "observed-data",
        "id": "observed-data--3cd23a7b-a099-49df-b397-189018311d4e",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa952",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-11-25T16:22:00.000Z",
        "first_observed": "2020-10-25T16:22:00Z",
        "last_observed": "2020-11-25T16:22:00Z",
        "number_observed": 1,
        "objects": {
            "0": {
                "type": "ipv4-addr",
                "value": "8.8.8.8"
            },
            "1": {
                "type": "ipv6-addr",
                "value": "2001:4860:4860::8888"
            }
        }
    },
    {
        "type": "observed-data",
        "id": "observed-data--3451329f-2525-4bcb-9659-7bd0e6f1eb0d",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa952",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "first_observed": "2020-10-25T16:22:00Z",
        "last_observed": "2020-10-25T16:22:00Z",
        "number_observed": 1,
        "objects": {
            "0": {
                "type": "ipv4-addr",
                "value": "185.194.93.14"
            }
        }
    }
]
_MAC_ADDRESS_ATTRIBUTES = [
    {
        "type": "observed-data",
        "id": "observed-data--3cd23a7b-a099-49df-b397-189018311d4e",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa952",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-11-25T16:22:00.000Z",
        "first_observed": "2020-10-25T16:22:00Z",
        "last_observed": "2020-11-25T16:22:00Z",
        "number_observed": 1,
        "objects": {
            "0": {
                "type": "mac-addr",
                "value": "d2:fb:49:24:37:18"
            },
            "1": {
                "type": "mac-addr",
                "value": "62:3e:5f:53:ac:68"
            }
        }
    },
    {
        "type": "observed-data",
        "id": "observed-data--3451329f-2525-4bcb-9659-7bd0e6f1eb0d",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa952",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "first_observed": "2020-10-25T16:22:00Z",
        "last_observed": "2020-10-25T16:22:00Z",
        "number_observed": 1,
        "objects": {
            "0": {
                "type": "mac-addr",
                "value": "ae:49:db:d4:d9:cf"
            }
        }
    }
]
_MALWARE_OBJECTS = [
    {
        "type": "malware",
        "id": "malware--2485b844-4efe-4343-84c8-eb33312dd56f",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa951",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "name": "MANITSME",
        "labels": [
            "backdoor",
            "dropper",
            "remote-access-trojan"
        ],
        "description": "This malware will beacon out at random intervals to the remote attacker. The attacker can run programs, execute arbitrary commands, and easily upload and download files."
    },
    {
        "type": "malware",
        "id": "malware--c0217091-9d3d-42a1-8952-ccc12d4ad8d0",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa951",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "name": "WEBC2-UGX",
        "labels": [
            "backdoor",
            "remote-access-trojan"
        ],
        "description": "A WEBC2 backdoor is designed to retrieve a Web page from a C2 server. It expects the page to contain special HTML tags; the backdoor will attempt to interpret the data between the tags as commands."
    }
]
_MUTEX_ATTRIBUTES = [
    {
        "type": "observed-data",
        "id": "observed-data--3cd23a7b-a099-49df-b397-189018311d4e",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa952",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-11-25T16:22:00.000Z",
        "first_observed": "2020-10-25T16:22:00Z",
        "last_observed": "2020-11-25T16:22:00Z",
        "number_observed": 1,
        "objects": {
            "0": {
                "type": "mutex",
                "name": "shared_resource_lock"
            },
            "1": {
                "type": "mutex",
                "name": "thread_synchronization_lock"
            }
        }
    },
    {
        "type": "observed-data",
        "id": "observed-data--3451329f-2525-4bcb-9659-7bd0e6f1eb0d",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa952",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "first_observed": "2020-10-25T16:22:00Z",
        "last_observed": "2020-10-25T16:22:00Z",
        "number_observed": 1,
        "objects": {
            "0": {
                "type": "mutex",
                "name": "sensitive_resource_lock"
            }
        }
    }
]
_SOFTWARE_OBJECTS = [
    {
        "type": "observed-data",
        "id": "observed-data--3cd23a7b-a099-49df-b397-189018311d4e",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa952",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-11-25T16:22:00.000Z",
        "first_observed": "2020-10-25T16:22:00Z",
        "last_observed": "2020-11-25T16:22:00Z",
        "number_observed": 1,
        "objects": {
            "0": {
                "type": "software",
                "name": "MISP",
                "languages": [
                    "PHP"
                ],
                "vendor": "MISP Project",
                "version": "2.4.183"
            },
            "1": {
                "type": "software",
                "name": "misp-stix",
                "languages": [
                    "Python"
                ],
                "vendor": "CIRCL",
                "version": "2.4.183"
            }
        }
    },
    {
        "type": "observed-data",
        "id": "observed-data--3451329f-2525-4bcb-9659-7bd0e6f1eb0d",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa952",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "first_observed": "2020-10-25T16:22:00Z",
        "last_observed": "2020-10-25T16:22:00Z",
        "number_observed": 1,
        "objects": {
            "0": {
                "type": "software",
                "name": "Acrobat X Pro",
                "cpe": "cpe:2.3:a:adobe:acrobat:10.0:-:pro:*:*:*:*:*",
                "swid": "<?xml version='1.0' encoding='utf-8'?><swid:software_identification_tag xsi:schemaLocation='https://standards.iso.org/iso/19770/-2/2008/schema.xsd software_identification_tag.xsd'xmlns:swid='https://standards.iso.org/iso/19770/-2/2008/schema.xsd' xmlns:xsi='https://www.w3.org/2001/XMLSchema-instance'><!--Mandatory Identity elements --><swid:entitlement_required_indicator>true</swid:entitlement_required_indicator><swid:product_title>Acrobat X Pro</swid:product_title><swid:product_version><swid:name>10.0</swid:name><swid:numeric><swid:major>10</swid:major><swid:minor>0</swid:minor><swid:build>0</swid:build><swid:review>0</swid:review></swid:numeric></swid:product_version><swid:software_creator><swid:name>Adobe Inc.</swid:name><swid:regid>regid.1986-12.com.adobe</swid:regid></swid:software_creator><swid:software_licensor><swid:name>Adobe Inc.</swid:name><swid:regid>regid.1986-12.com.adobe</swid:regid></swid:software_licensor><swid:software_id><swid:unique_id>AcrobatPro-AS1-Win-GM-MUL</swid:unique_id><swid:tag_creator_regid>regid.1986-12.com.adobe</swid:tag_creator_regid></swid:software_id><swid:tag_creator><swid:name>Adobe Inc.</swid:name><swid:regid>regid.1986-12.com.adobe</swid:regid></swid:tag_creator><!--Optional Identity elements --><swid:license_linkage><swid:activation_status>unlicensed</swid:activation_status><swid:channel_type>VOLUME</swid:channel_type><swid:customer_type>VOLUME</swid:customer_type></swid:license_linkage><swid:serial_number>970787034620329571838915</swid:serial_number></swid:software_identification_tag>",
                "languages": [
                    "C#",
                    "Javascript",
                    "Postscript"
                ],
                "vendor": "Adobe Inc.",
                "version": "10.0"
            }
        }
    }
]
_THREAT_ACTOR_OBJECTS = [
    {
        "type": "threat-actor",
        "id": "threat-actor--6d179234-61fc-40c4-ae86-3d53308d8e65",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa951",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "name": "Ugly Gorilla",
        "labels": [
            "nation-state",
            "spy"
        ],
        "roles": [
            "malware-author",
            "agent",
            "infrastructure-operator"
        ],
        "resource_level": "government",
        "aliases": [
            "Greenfield",
            "JackWang",
            "Wang Dong"
        ],
        "primary_motivation": "organizational-gain"
    },
    {
        "type": "threat-actor",
        "id": "threat-actor--d84cf283-93be-4ca7-890d-76c63eff3636",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa951",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "name": "DOTA",
        "labels": [
            "nation-state",
            "spy"
        ],
        "aliases": [
            "dota",
            "Rodney",
            "Raith"
        ],
        "resource_level": "government",
        "roles": [
            "agent",
            "infrastructure-operator"
        ],
        "primary_motivation": "organizational-gain"
    }
]
_TOOL_OBJECTS = [
    {
        "type": "tool",
        "id": "tool--ce45f721-af14-4fc0-938c-000c16186418",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa951",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "name": "cachedump",
        "labels": [
            "credential-exploitation"
        ],
        "description": "This program extracts cached password hashes from a system’s registry.",
        "kill_chain_phases": [
            {
                "kill_chain_name": "mandiant-attack-lifecycle-model",
                "phase_name": "escalate-privileges"
            }
        ]
    },
    {
        "type": "tool",
        "id": "tool--e9778c42-bc2f-4eda-9fb4-6a931834f68c",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa951",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "name": "fgdump",
        "labels": [
            "credential-exploitation"
        ],
        "description": "Windows password hash dumper",
        "kill_chain_phases": [
            {
                "kill_chain_name": "mandiant-attack-lifecycle-model",
                "phase_name": "escalate-privileges"
            }
        ],
        "external_references": [
            {
                "source_name": "fgdump",
                "url": "http://www.foofus.net/fizzgig/fgdump/"
            }
        ]
    }
]
_URL_ATTRIBUTES = [
    {
        "type": "observed-data",
        "id": "observed-data--3cd23a7b-a099-49df-b397-189018311d4e",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa952",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-11-25T16:22:00.000Z",
        "first_observed": "2020-10-25T16:22:00Z",
        "last_observed": "2020-11-25T16:22:00Z",
        "number_observed": 1,
        "objects": {
            "0": {
                "type": "url",
                "value": "https://circl.lu/team/"
            },
            "1": {
                "type": "url",
                "value": "https://cybersecurity.lu/entity/324"
            }
        }
    },
    {
        "type": "observed-data",
        "id": "observed-data--3451329f-2525-4bcb-9659-7bd0e6f1eb0d",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa952",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "first_observed": "2020-10-25T16:22:00Z",
        "last_observed": "2020-10-25T16:22:00Z",
        "number_observed": 1,
        "objects": {
            "0": {
                "type": "url",
                "value": "https://misp-project.org/blog/"
            }
        }
    }
]
_VULNERABILITY_OBJECTS = [
    {
        "type": "vulnerability",
        "id": "vulnerability--c7cab3fb-0822-43a5-b1ba-c9bab34361a2",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa951",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "name": "CVE-2012-0158",
        "description": "Weaponized Microsoft Word document used by admin@338",
        "external_references": [
            {
                "source_name": "cve",
                "external_id": "CVE-2012-0158"
            }
        ]
    },
    {
        "type": "vulnerability",
        "id": "vulnerability--6a2eab9c-9789-4437-812b-d74323fa3bca",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa951",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "name": "CVE-2009-4324",
        "description": "Adobe acrobat PDF's used by admin@338",
        "external_references": [
            {
                "source_name": "cve",
                "external_id": "CVE-2009-4324"
            }
        ]
    }
]


class TestExternalSTIX20Bundles:
    __bundle = {
        "type": "bundle",
        "id": "bundle--314e4210-e41a-4952-9f3c-135d7d577112",
        "spec_version": "2.0"
    }
    __identity = {
        "type": "identity",
        "id": "identity--a0c22599-9e58-4da4-96ac-7051603fa951",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "name": "MISP-Project",
        "identity_class": "organization"
    }
    __report = {
        "type": "report",
        "id": "report--a6ef17d6-91cb-4a05-b10b-2f045daf874c",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa951",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "name": "MISP-STIX-Converter test event",
        "published": "2020-10-25T16:22:00Z",
        "labels": [
            "Threat-Report",
            "misp:tool=\"MISP-STIX-Converter\""
        ]
    }
    __indicator = {
        "type": "indicator",
        "id": "indicator--031778a4-057f-48e6-9db9-c8d72b81ccd5",
        "created_by_ref": "identity--a0c22599-9e58-4da4-96ac-7051603fa951",
        "created": "2020-10-25T16:22:00.000Z",
        "modified": "2020-10-25T16:22:00.000Z",
        "name": "HTRAN Hop Point Accessor",
        "description": "Test description.",
        "pattern": "[ipv4-addr:value = '223.166.0.0/15']",
        "labels": [
            "malicious-activity"
        ],
        "valid_from": "2020-10-25T16:22:00.000Z",
        "kill_chain_phases": [
            {
                "kill_chain_name": "mandiant-attack-lifecycle-model",
                "phase_name": "establish-foothold"
            }
        ]
    }

    @classmethod
    def __assemble_bundle(cls, *stix_objects):
        bundle = deepcopy(cls.__bundle)
        bundle['objects'] = [
            deepcopy(cls.__identity), deepcopy(cls.__report), *stix_objects
        ]
        bundle['objects'][1]['object_refs'] = [
            stix_object['id'] for stix_object in stix_objects
        ]
        return dict_to_stix2(bundle, allow_custom=True)

    @classmethod
    def __assemble_galaxy_bundle(cls, event_galaxy, attribute_galaxy):
        relationship = {
            "type": "relationship",
            "id": "relationship--7cede760-b866-490e-ad5b-1df34bc14f8d",
            "created": "2020-10-25T16:22:00.000Z",
            "modified": "2020-10-25T16:22:00.000Z",
            "relationship_type": "indicates",
            "source_ref": cls.__indicator['id'],
            "target_ref": attribute_galaxy['id']
        }
        bundle = deepcopy(cls.__bundle)
        bundle['objects'] = [
            deepcopy(cls.__identity), deepcopy(cls.__report),
            event_galaxy, cls.__indicator, attribute_galaxy, relationship
        ]
        bundle['objects'][1]['object_refs'] = [
            stix_object['id'] for stix_object in bundle['objects'][2:]
        ]
        return dict_to_stix2(bundle, allow_custom=True)

    ############################################################################
    #                             GALAXIES SAMPLES                             #
    ############################################################################

    @classmethod
    def get_bundle_with_attack_pattern_galaxy(cls):
        return cls.__assemble_galaxy_bundle(*_ATTACK_PATTERN_OBJECTS)

    @classmethod
    def get_bundle_with_campaign_galaxy(cls):
        return cls.__assemble_galaxy_bundle(*_CAMPAIGN_OBJECTS)

    @classmethod
    def get_bundle_with_course_of_action_galaxy(cls):
        return cls.__assemble_galaxy_bundle(*_COURSE_OF_ACTION_OBJECTS)

    @classmethod
    def get_bundle_with_intrusion_set_galaxy(cls):
        return cls.__assemble_galaxy_bundle(*_INTRUSION_SET_OBJECTS)

    @classmethod
    def get_bundle_with_malware_galaxy(cls):
        return cls.__assemble_galaxy_bundle(*_MALWARE_OBJECTS)

    @classmethod
    def get_bundle_with_threat_actor_galaxy(cls):
        return cls.__assemble_galaxy_bundle(*_THREAT_ACTOR_OBJECTS)

    @classmethod
    def get_bundle_with_tool_galaxy(cls):
        return cls.__assemble_galaxy_bundle(*_TOOL_OBJECTS)

    @classmethod
    def get_bundle_with_vulnerability_galaxy(cls):
        return cls.__assemble_galaxy_bundle(*_VULNERABILITY_OBJECTS)

    ############################################################################
    #                          OBSERVED DATA SAMPLES.                          #
    ############################################################################

    @classmethod
    def get_bundle_with_artifact_objects(cls):
        return cls.__assemble_bundle(*_ARTIFACT_OBJECTS)

    @classmethod
    def get_bundle_with_as_objects(cls):
        return cls.__assemble_bundle(*_AS_OBJECTS)

    @classmethod
    def get_bundle_with_directory_objects(cls):
        return cls.__assemble_bundle(*_DIRECTORY_OBJECTS)

    @classmethod
    def get_bundle_with_domain_attributes(cls):
        return cls.__assemble_bundle(*_DOMAIN_ATTRIBUTES)

    @classmethod
    def get_bundle_with_email_address_attributes(cls):
        return cls.__assemble_bundle(*_EMAIL_ADDRESS_ATTRIBUTES)

    @classmethod
    def get_bundle_with_ip_address_attributes(cls):
        return cls.__assemble_bundle(*_IP_ADDRESS_ATTRIBUTES)

    @classmethod
    def get_bundle_with_mac_address_attributes(cls):
        return cls.__assemble_bundle(*_MAC_ADDRESS_ATTRIBUTES)

    @classmethod
    def get_bundle_with_mutex_attributes(cls):
        return cls.__assemble_bundle(*_MUTEX_ATTRIBUTES)

    @classmethod
    def get_bundle_with_software_objects(cls):
        return cls.__assemble_bundle(*_SOFTWARE_OBJECTS)

    @classmethod
    def get_bundle_with_url_attributes(cls):
        return cls.__assemble_bundle(*_URL_ATTRIBUTES)
