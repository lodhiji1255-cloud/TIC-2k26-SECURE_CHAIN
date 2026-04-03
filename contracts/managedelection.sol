/ SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ManageElection {
    struct Candidate {
        uint id;
        string name;
        uint voteCount;
    }
     mapping(uint => Candidate) public candidates;
    uint public candidateCount;

    // enrollment -> has voted?
    mapping(string => bool) public hasVoted;

    // faceHash (bytes32) -> used for voting?
    mapping(bytes32 => bool) public usedFace;

    // faceHash -> registered?
    mapping(bytes32 => bool) public registeredFace;

    // enrollment -> registered?
    mapping(string => bool) public registeredEnrollment;
    // event for blockchain alert
    event CandidateAdded(uint id, string name);
    event VoterRegistered(string enrollment, bytes32 faceHash);
    event Voted(string enrollment, bytes32 faceHash, uint candidateId);
} 